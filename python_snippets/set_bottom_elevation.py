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
PARAM_QUERY = "ACM_EC_Absolute Elevation"
PARAM_TARGET = "ACM_CSD_BotOfEle"

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝

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
tg = TransactionGroup(doc, "Set String Elevation")
tg.Start()
try:
    t1 = Transaction(doc, "Refresh Horizontal Duct Elevation")
    t1.Start()
    ducts = []
    try:
        for duct in duct_collector:
            query_res = duct.LookupParameter(PARAM_QUERY).AsValueString()
            if query_res and query_res != "":
                duct.LookupParameter(PARAM_TARGET).Set(query_res)
                ducts.append(query_res)
            else:
                duct.LookupParameter(PARAM_TARGET).Set("-")
                ducts.append("-")
    except Exception as e1:
        ducts.append("Error processing duct ID {}: {}".format(duct.Id, e1))
    t1.Commit()

    t2 = Transaction(doc, "Refresh Horizontal Cable Tray Elevation")
    t2.Start()
    cable_trays = []
    try:
        for cable_tray in cable_tray_collector:
            query_res = cable_tray.LookupParameter(PARAM_QUERY).AsValueString()
            if query_res and query_res != "":
                cable_tray.LookupParameter(PARAM_TARGET).Set(query_res)
                cable_trays.append(query_res)
            else:
                cable_tray.LookupParameter(PARAM_TARGET).Set("-")
                cable_trays.append("-")
    except Exception as e2:
        cable_trays.append("Error processing cable tray ID {}: {}".format(cable_tray.Id, e2))
    t2.Commit()

    t3 = Transaction(doc, "Refresh Horizontal Pipe Elevation")
    t3.Start()
    pipes = []
    try:
        for pipe in pipe_collector:
            query_res = pipe.LookupParameter(PARAM_QUERY).AsValueString()
            if query_res and query_res != "":
                pipe.LookupParameter(PARAM_TARGET).Set(query_res)
                pipes.append(query_res)
            else:
                pipe.LookupParameter(PARAM_TARGET).Set("-")
                pipes.append("-")
    except Exception as e3:
        pipes.append("Error processing pipe ID {}: {}".format(pipe.Id, e3))
    t3.Commit()

    t4 = Transaction(doc, "Refresh Horizontal Conduit Elevation")
    t4.Start()
    conduits = []
    try:
        for conduit in conduit_collector:
            query_res = conduit.LookupParameter(PARAM_QUERY).AsValueString()
            if query_res and query_res != "":
                conduit.LookupParameter(PARAM_TARGET).Set(query_res)
                conduits.append(query_res)
            else:
                conduit.LookupParameter(PARAM_TARGET).Set("-")
                conduits.append("-")
    except Exception as e4:
        conduits.append("Error processing conduit ID {}: {}".format(conduit.Id, e4))
    t4.Commit()
except Exception as e:
     print("Error in transaction: {}".format(e))
     tg.RollBack()
tg.Assimilate()

OUT = ducts, cable_trays, pipes, conduits