import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

scheduleType = IN[0]

countLimit = []

if scheduleType == "EE CABLE TRAYS SCHEDULE":
    limit = 246
    countLimit.append(limit)
elif scheduleType == "EE DUCTS SCHEDULE":
    limit = 328
    countLimit.append(limit)
elif scheduleType == "EE CABLE TRAY FITTINGS SCHEDULE":
    limit = 328
    countLimit.append(limit)
elif scheduleType == "EE CONDUITS SCHEDULE":
    limit = 328
    countLimit.append(limit)
elif scheduleType == "GENERAL CABLE TRAYS SCHEDULE":
    limit = 246
    countLimit.append(limit)
elif scheduleType == "GENERAL PIPES SCHEDULE":
    limit = 328
    countLimit.append(limit)
elif scheduleType == "GENERAL DUCTS SCHEDULE":
    limit = 328
    countLimit.append(limit)

# Assign the list of points to the OUT variable.
OUT = countLimit