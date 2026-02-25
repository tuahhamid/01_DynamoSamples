import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('System')
from System.Collections.Generic import List

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗  
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗  
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝  
tagging_parameter = "ACM_EC_Absolute Elevation"
tolerance = 1e-6

def set_elev_parameter(tagging_parameter, element, value): # type: (str, Element, float) -> None
    '''Set the elevation parameter to the element'''
    param = element.LookupParameter(tagging_parameter)
    if param:
        try:
            param.Set(value)
        except:
            print("Failed to set parameter {tagging_parameter} for element {element.Id}. Value: {value}".format())

def is_close_to_zero(direction, tolerance): # type: (float, float) -> bool
    '''Check if the current direction value is close or equal to zero'''
    is_valid = False
    if abs(1 - abs(direction)) > tolerance:
        is_valid = True
    return is_valid

duct_collector = FilteredElementCollector(doc)\
                .OfCategory(BuiltInCategory.OST_DuctCurves)\
                .WhereElementIsNotElementType()\
                .ToElements()

cable_tray_collector = FilteredElementCollector(doc)\
                .OfCategory(BuiltInCategory.OST_CableTray)\
                .WhereElementIsNotElementType()\
                .ToElements()

pipe_collector = FilteredElementCollector(doc)\
                .OfCategory(BuiltInCategory.OST_PipeCurves)\
                .WhereElementIsNotElementType()\
                .ToElements()

conduit_collector = FilteredElementCollector(doc)\
                .OfCategory(BuiltInCategory.OST_Conduit)\
                .WhereElementIsNotElementType()\
                .ToElements()

#Do some action in a Transaction
tg = TransactionGroup(doc, "Refresh Elevation")
tg.Start()

try:
    # horizontal ducts transaction
    # change compare to 0 logic for floating point data
    t1 = Transaction(doc, "Refresh Horizontal Duct Elevation")
    t1.Start()
    ducts = []
    for duct in duct_collector:
        duct_direction = duct.Location.Curve.Direction.Z # type: float
        duct_shape = duct.DuctType.Shape
        valid_duct = is_close_to_zero(duct_direction, tolerance)
        if valid_duct and duct_shape != ConnectorProfileType.Round:
            try:
                    # print("Duct ID: {} - Direction: {}".format(duct.Id, direction))
                    ducts.append(duct)
                    duct_height = duct.Height / 2 
                    duct_elevation = duct.Location.Curve.Origin.Z
                    duct_insulation_id = InsulationLiningBase.GetInsulationIds(doc, duct.Id)
                    if duct_insulation_id:
                        duct_insulation_element = doc.GetElement(duct_insulation_id[0])
                        duct_insulation_thickness = duct_insulation_element.Thickness
                        new_val = duct_elevation - duct_height - duct_insulation_thickness
                    else:
                        new_val = duct_elevation - duct_height
                    set_elev_parameter(tagging_parameter, duct, new_val)
            except Exception as e1:
                ducts.append("Error processing duct ID {}: {}".format(duct.Id, e1))
    t1.Commit()

    # cable trays transaction
    t2 = Transaction(doc, "Refresh Horizontal Cable Tray Elevation")
    t2.Start()
    cable_trays = []
    for cable_tray in cable_tray_collector:
        ct_direction = cable_tray.Location.Curve.Direction.Z # type: float
        valid_ct = is_close_to_zero(ct_direction, tolerance)
        if valid_ct:
            try:
                cable_trays.append(cable_tray)
                cable_tray_height = cable_tray.Height / 2
                cable_tray_elevation = cable_tray.Location.Curve.Origin.Z
                new_val = cable_tray_elevation - cable_tray_height
                set_elev_parameter(tagging_parameter, cable_tray, new_val)
            except Exception as e2:
                cable_trays.append("Error processing cable tray ID {}: {}".format(cable_tray.Id, e2))
    t2.Commit()
    
    # horizontal pipes transaction
    # formula = Outer diameter / 2 + Insulation thickness
    t3 = Transaction(doc, "Refresh Horizontal Pipe Elevation")
    t3.Start()
    pipes = []
    for pipe in pipe_collector:
        pipe_direction = pipe.Location.Curve.Direction.Z # type: float
        valid_pipe = is_close_to_zero(pipe_direction, tolerance)
        if valid_pipe:
            try:
                pipes.append(pipe)
                pipe_elev = pipe.Location.Curve.Origin.Z
                outer_radius = pipe.get_Parameter(BuiltInParameter.RBS_PIPE_OUTER_DIAMETER).AsDouble() / 2
                insulation_id = InsulationLiningBase.GetInsulationIds(doc, pipe.Id)

                # calculate new bottom of pipe elevation
                if insulation_id:
                    insulation_element = doc.GetElement(insulation_id[0])
                    insulation_thickness = insulation_element.Thickness
                    new_val = pipe_elev - outer_radius - insulation_thickness
                    set_elev_parameter(tagging_parameter, pipe, new_val)
                else:
                    new_val = pipe_elev - outer_radius
                    set_elev_parameter(tagging_parameter, pipe, new_val)
            except Exception as e3:
                pipes.append("Error processing pipe ID {}: {}".format(pipe.Id, e3))
    t3.Commit()

        # horizontal conduits transaction
    t4 = Transaction(doc, "Refresh Horizontal Conduit Elevation")
    t4.Start()
    conduits = []
    for conduit in conduit_collector:
        conduit_direction = conduit.Location.Curve.Direction.Z # type: float
        valid_conduit = is_close_to_zero(conduit_direction, tolerance)
        if valid_conduit:
            try:
                conduits.append(conduit)
                conduit_elev = conduit.Location.Curve.Origin.Z
                outer_radius = conduit.get_Parameter(BuiltInParameter.RBS_CONDUIT_OUTER_DIAM_PARAM).AsDouble() / 2
                new_val = conduit_elev - outer_radius
                set_elev_parameter(tagging_parameter, conduit, new_val)
            except Exception as e4:
                # set_elev_parameter(PARAM_NAME, conduit, "-")
                conduits.append("Error processing conduit ID {}: {}".format(conduit.Id, e4))
    t4.Commit()

    tg.Assimilate()

except Exception as e:
    print("Error in transaction: {}".format(e))
    tg.RollBack()

OUT = ducts, cable_trays, pipes, conduits