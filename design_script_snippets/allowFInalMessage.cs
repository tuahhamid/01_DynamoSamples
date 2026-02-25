elements;
paramName = "ACM_CSD_Obj ID";
value;

//set Object ID values
setParam = Revit.Elements.Element.SetParameterByName
(elements, paramName, value);
tr = Transaction.End(setParam);

dataA = value[0];
dataZ = value[-1];
testData = List.IsEmpty(value);
isNull = DSCore.Object.IsNull(value);

allowMessage = [Imperative]
{
	if (testData == true || isNull == true)
		return List.Empty;
	else
		return successMessage(dataA, dataZ);
};

"Result!";
allowMessage;