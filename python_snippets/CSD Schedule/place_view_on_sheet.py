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

dyn_sheets = IN[0]
dyn_sheetsviews = IN[1]
sheets = [UnwrapElement(sheet) for sheet in dyn_sheets]
views = [UnwrapElement(view) for view in dyn_sheetsviews]
x_loc = 65
y_loc = 575
location = XYZ(
                UnitUtils.ConvertToInternalUnits(x_loc, UnitTypeId.Millimeters), 
                UnitUtils.ConvertToInternalUnits(y_loc, UnitTypeId.Millimeters), 
                0)

sch_instances = []

TransactionManager.Instance.EnsureInTransaction(doc)

for sheet, view in zip(sheets, views):
    sch_instance = ScheduleSheetInstance.Create(doc, sheet.Id, view.Id, location)
    sch_instances.append(sch_instance)

TransactionManager.Instance.TransactionTaskDone()

OUT = sch_instances, sheets