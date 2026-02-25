import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

scheduleType = IN[0]

points = None

if scheduleType == "EE CABLE TRAYS SCHEDULE":
    point1 = Point.ByCoordinates(65, 575, 0)
    point2 = Point.ByCoordinates(290, 575, 0)
    point3 = Point.ByCoordinates(515, 575, 0)
    points = [point1, point2, point3]
elif scheduleType == "EE DUCTS SCHEDULE":
    point1 = Point.ByCoordinates(73.5, 575, 0)
    point2 = Point.ByCoordinates(248.5, 575, 0)
    point3 = Point.ByCoordinates(423.5, 575, 0)
    point4 = Point.ByCoordinates(598.5, 575, 0)
    points = [point1, point2, point3, point4]
elif scheduleType == "EE CABLE TRAY FITTINGS SCHEDULE":
    point1 = Point.ByCoordinates(83.5, 575, 0)
    point2 = Point.ByCoordinates(318.5, 575, 0)
    point3 = Point.ByCoordinates(553.5, 575, 0)
    point4 = Point.ByCoordinates(788.5, 575, 0)
    points = [point1, point2, point3, point4]
elif scheduleType == "EE CONDUITS SCHEDULE":
    point1 = Point.ByCoordinates(83.5, 575, 0)
    point2 = Point.ByCoordinates(243.5, 575, 0)
    point3 = Point.ByCoordinates(403.5, 575, 0)
    point4 = Point.ByCoordinates(563.5, 575, 0)
    points = [point1, point2, point3, point4]
elif scheduleType == "GENERAL CABLE TRAYS SCHEDULE":
    point1 = Point.ByCoordinates(53.5, 575, 0)
    point2 = Point.ByCoordinates(278.5, 575, 0)
    point3 = Point.ByCoordinates(503.5, 575, 0)
    points = [point1, point2, point3]
elif scheduleType == "GENERAL PIPES SCHEDULE":
    point1 = Point.ByCoordinates(83.5, 575, 0)
    point2 = Point.ByCoordinates(243.5, 575, 0)
    point3 = Point.ByCoordinates(403.5, 575, 0)
    point4 = Point.ByCoordinates(563.5, 575, 0)
    points = [point1, point2, point3, point4]
elif scheduleType == "GENERAL DUCTS SCHEDULE":
    point1 = Point.ByCoordinates(73.5, 575, 0)
    point2 = Point.ByCoordinates(248.5, 575, 0)
    point3 = Point.ByCoordinates(423.5, 575, 0)
    point4 = Point.ByCoordinates(598.5, 575, 0)
    points = [point1, point2, point3, point4]

# Assign the list of points to the OUT variable.
OUT = points