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

spFile = IN[0]
param_names = IN[1]
cat_set_list = IN[2]

PARAM_GROUP_NAME = "22 CSD"
sp_groups = spFile.Groups

stats = []

TransactionManager.Instance.EnsureInTransaction(doc)

for p, c, in zip(param_names, cat_set_list):
    for spg in sp_groups:
        if spg.Name == PARAM_GROUP_NAME:
            for defn in spg.Definitions:
                if defn.Name in param_names:
                    doc.ParameterBindings.Insert(
                        defn,
                        InstanceBinding(cat_set_list),
                        GroupTypeId.IdentityData)

TransactionManager.Instance.TransactionTaskDone()

OUT = stats