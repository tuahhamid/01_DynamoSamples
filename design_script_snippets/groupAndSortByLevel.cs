busducts;
others;
modelCode;

//sort busduct elements using elevation as keys
busductElev = Revit.Elements.Element.GetParameterValueByName
(busducts, "ACM_CSD_Elevation");
busductDict = Orchid.List.GroupByKey(busducts@L2<1>, busductElev@L2<1>, true);
sortedBusduct = Dictionary.ValueAtKey(busductDict, "d0");
busductKeys = Dictionary.ValueAtKey(busductDict, "d1");

//sort other elements using elevation as keys
otherElev = Revit.Elements.Element.GetParameterValueByName
(others, "ACM_CSD_Elevation");
othersDict = Orchid.List.GroupByKey(others@L2<1>, otherElev@L2<1>, true);
sortedOthers = Dictionary.ValueAtKey(othersDict, "d0");
othersKeys = Dictionary.ValueAtKey(othersDict, "d1");

//output
joinedList = List.Join
([(List.Flatten(sortedOthers, -1)), (List.Flatten(sortedBusduct, -1))]);
modelCode;