scheduleType = IN[0]
segHeights = None

if scheduleType == "EE CABLE TRAYS SCHEDULE":
    segHeights = [485, 485]
    # segHeights.append(segHeights)
elif scheduleType == "EE DUCTS SCHEDULE":
    segHeights = [485, 485, 485]
    # segHeights.append(segHeights)
elif scheduleType == "EE CABLE TRAY FITTINGS SCHEDULE":
    segHeights = [485, 485, 485]
    # segHeights.append(segHeights)
elif scheduleType == "EE CONDUITS SCHEDULE":
    segHeights = [485, 485, 485]
    # segHeights.append(segHeights)
elif scheduleType == "GENERAL CABLE TRAYS SCHEDULE":
    segHeights = [485, 485]
    # segHeights.append(segHeights)
elif scheduleType == "GENERAL PIPES SCHEDULE":
    segHeights = [485, 485, 485]
    # segHeights.append(segHeights)
elif scheduleType == "GENERAL DUCTS SCHEDULE":
    segHeights = [485, 485, 485]
    # segHeights.append(segHeights)
# Assign the list of points to the OUT variable.
OUT = segHeights
