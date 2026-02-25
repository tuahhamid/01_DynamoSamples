scheduleType = IN[0]
indexes = None

if scheduleType == "EE CABLE TRAYS SCHEDULE":
    indexes = [0,1,2]
    # indexes.append(ind)
elif scheduleType == "EE DUCTS SCHEDULE":
    indexes = [0,1,2,3]
    # indexes.append(indexes)
elif scheduleType == "EE CABLE TRAY FITTINGS SCHEDULE":
    indexes = [0,1,2,3]
    # indexes.append(indexes)
elif scheduleType == "EE CONDUITS SCHEDULE":
    indexes = [0,1,2,3]
    # indexes.append(indexes)
elif scheduleType == "GENERAL CABLE TRAYS SCHEDULE":
    indexes = [0,1,2]
    # indexes.append(indexes)
elif scheduleType == "GENERAL PIPES SCHEDULE":
    indexes = [0,1,2,3]
    # indexes.append(indexes)
elif scheduleType == "GENERAL DUCTS SCHEDULE":
    indexes = [0,1,2,3]
    # indexes.append(ind)

# Assign the list of points to the OUT variable.
OUT = indexes