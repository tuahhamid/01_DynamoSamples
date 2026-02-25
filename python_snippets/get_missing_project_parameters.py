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

req_params = IN[0] # type: List[str]

bm = doc.ParameterBindings

itor = bm.ForwardIterator()
itor.Reset()

param_names = []
while itor.MoveNext():
	d = itor.Key
	param_names.append(d.Name)

missing = []
for p in req_params:
	if p not in param_names:
		missing.append(p)

OUT = missing