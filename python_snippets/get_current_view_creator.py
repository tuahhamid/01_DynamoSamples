import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

#Preparing input from dynamo to revit
elements = IN[0] # as Active View

if isinstance(elements, list):
    unwrapped_elements = [UnwrapElement(ele) for ele in elements]
else:
     unwrapped_elements = UnwrapElement(elements)

view_id_str = unwrapped_elements.Id.ToString()
view_creator = WorksharingUtils.GetWorksharingTooltipInfo(doc, unwrapped_elements.Id).Creator


OUT = view_creator