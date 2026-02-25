cableTrays;
conduits;
busducts;

//get valid cable trays
//ORL get all elements of CT
validCb = cableTrays;

//get valid conduits conduits
conduitSizes = Revit.Elements.Element.GetParameterValueByName(conduits, "Size");
testConduit = conduitSizes == "ø160";
countConduit = List.Count(conduits);
indCoundits = testConduit == true?-1:0..countConduit-1;
validConduits = List.RemoveItemAtIndex(conduits, indCoundits);

//get valid busducts
busductNames = Revit.Elements.Element.Name(busducts);
testBusducts = DSCore.String.StartsWith(busductNames, "Cu", true);
countBusducts = List.Count(busducts);
indBusduct = testBusducts==true?-1:0..countBusducts-1;
validBusducts = List.RemoveItemAtIndex(busducts, indBusduct);

//output
validCb;
validConduits;
validBusducts;
newList = [validCb, validConduits, validBusducts];