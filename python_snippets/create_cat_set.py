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

PARAM_GROUP_NAME = ["22 CSD", "10 Mechanical"]
sp_file = IN[0]
params_to_insert = IN[1]
sp_groups = sp_file.Groups

# ╔═╗╔═╗╔╦╗╔═╗╔═╗╔═╗╦═╗╦╔═╗╔═╗  ╔═╗╔═╗╔╦╗
# ║  ╠═╣ ║ ║╣ ║ ╦║ ║╠╦╝║║╣ ╚═╗  ╚═╗║╣  ║ 
# ╚═╝╩ ╩ ╩ ╚═╝╚═╝╚═╝╩╚═╩╚═╝╚═╝  ╚═╝╚═╝ ╩ 

req_param_names = [
            "ACM_CSD_Amp Rating", # 0
            "ACM_CSD_Elevation", # 1
            "ACM_CSD_Level Ref", # 2
            "ACM_CSD_Obj ID", # 3
            "ACM_EC_Absolute Elevation", # 4
        ]

bic_map = [
    [BuiltInCategory.OST_CableTrayFitting], # -2008126
    # [BuiltInCategory.OST_Conduit], # -2008132
    # [BuiltInCategory.OST_DuctCurves], # -2008000
    # [BuiltInCategory.OST_PipeCurves], # -2008044
    # [BuiltInCategory.OST_CableTray], # -2008130
    [
        BuiltInCategory.OST_CableTray,
        BuiltInCategory.OST_CableTrayFitting,
        BuiltInCategory.OST_DuctCurves,
        BuiltInCategory.OST_PipeCurves,
        BuiltInCategory.OST_Conduit
    ]
]

def create_cat_set(bic_map):
    cat_set = CategorySet()
    for bic in bic_map:
        cat_set.Insert(Category.GetCategory(doc, bic))
    return cat_set

def get_set_type(def_name, bic_map):
    if def_name == req_param_names[0]:
        map_set = bic_map[0]
    else:
        map_set = bic_map[1]
    return map_set

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝

TransactionManager.Instance.EnsureInTransaction(doc)

for spg in sp_groups:
    typ_g = []
    if spg.Name in PARAM_GROUP_NAME:
        defns = spg.Definitions
        typ_res = []
        for defn in defns:
            if defn.Name in params_to_insert and defn.Name in req_param_names:
                cat_set = create_cat_set(get_set_type(defn.Name, bic_map))
                typ_res.append(cat_set)
                doc.ParameterBindings.Insert(
                    defn,
                    InstanceBinding(cat_set),
                    GroupTypeId.IdentityData)
        typ_g.append(typ_res)

TransactionManager.Instance.TransactionTaskDone()

OUT = typ_g, params_to_insert