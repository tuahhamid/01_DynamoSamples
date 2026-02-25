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
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

sp_file = app.OpenSharedParameterFile()
param_groups = sp_file.Groups

required_names = IN[0]
required_groups = IN[1]

group_names = []
for pg in param_groups:
	group_names.append(pg.Name)

not_found_groups = []
not_found_defs = []

for req_g in required_groups:
    if req_g not in group_names:
        not_found_groups.append(req_g)

for req_name in required_names:
	found = False
	for pg in param_groups:
		for defn in pg.Definitions:
			if defn.Name == req_name:
				found = True
				break
		if found:
			break
	if not found:
		not_found_defs.append(req_name)



# if empty lists, all required groups/defs were found
OUT = not_found_groups, not_found_defs, sp_file.Filename