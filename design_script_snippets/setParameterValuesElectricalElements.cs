modelCode;
elements;

//test empty
testEmpty = List.IsEmpty(elements@L2<1>);
countList = List.Count(elements);
indX = testEmpty==false?-1:0..countList-1;
validElements = List.RemoveItemAtIndex(elements, indX);

//seperate busducts from others
category = Revit.Elements.Element.GetCategory(validElements);
catNames = Revit.Category.Name(category);
testBusducts = List.Contains(catNames@L2<1>, "Cable Tray Fittings");
elemDict = List.FilterByBoolMask(validElements, testBusducts);
busducts = List.Flatten(Dictionary.ValueAtKey(elemDict, "in"), -1);
others = Dictionary.ValueAtKey(elemDict, "out");

//set Reference Level ID for busducts
busductLevels = Revit.Elements.Element.GetParameterValueByName(busducts, "Level");
busductLevelNames = Revit.Elements.Element.Name(busductLevels);
setBusductLevelParam = Revit.Elements.Element.SetParameterByName(busducts, "ACM_CSD_Level Ref", busductLevelNames);

//set ACM_CSD_Elevation for busducts
busductLevelValues = Revit.Elements.Element.GetParameterValueByName(busductLevels, "Elevation");
setBusductEleValue = Revit.Elements.Element.SetParameterByName(busducts, "ACM_CSD_Elevation", busductLevelValues);

//set ACM_CSD_Amp Rating for busducts
busductNames = Revit.Elements.Element.Name(busducts);
splitBusductNames = DSCore.String.Split(busductNames, [" "]);
getRatingValues = List.GetItemAtIndex(splitBusductNames@L2<1>, 1);
element2 = Revit.Elements.Element.SetParameterByName(busducts, "ACM_CSD_Amp Rating", getRatingValues);

//set Reference Level ID for others
othersLevels = Revit.Elements.Element.GetParameterValueByName(others, "Reference Level");
othersLevelNames = Revit.Elements.Element.Name(othersLevels);
setOthersLevelParam = Revit.Elements.Element.SetParameterByName(others, "ACM_CSD_Level Ref", othersLevelNames);

//set ACM_CSD_Elevation for others
othersLevelValues = Number.ToInteger(Revit.Elements.Element.GetParameterValueByName(othersLevels, "Elevation"));
setOthersEleValue = Revit.Elements.Element.SetParameterByName(others, "ACM_CSD_Elevation", othersLevelValues);

//output
outBusduct = Transaction.End(busducts);
outOthers = Transaction.End(others);
modelCode;