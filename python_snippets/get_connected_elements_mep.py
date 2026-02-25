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

def get_connected_elements(element):
    try:
        connectors = element.ConnectorManager.Connectors
    except:
        connectors = element.MEPModel.ConnectorManager.Connectors

    connected_elements = []
    for connector in connectors:
        for connected_connector in connector.AllRefs:
            connected_element = connected_connector.Owner
            if connected_element.Id != element.Id and "System" not in connected_element.Category.Name:
                connected_elements.append(connected_element)
    return connected_elements

start_element = UnwrapElement(IN[0])

OUT = get_connected_elements(start_element)