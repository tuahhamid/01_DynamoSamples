res;
paramNamesToInsert;
mergedNames;

isEmpty = List.IsEmpty(res);
isNull = List.Contains(DSCore.Object.IsNull(List.Flatten(res, -1)), true);

successMessage = "Successfully added the following parameters to the project: " + "\n" + mergedNames;

allowMessage = [Imperative]{
if (isNull == true || isEmpty == true)
	return List.Empty;
else
	return successMessage;
};

//output
"Result!";
allowMessage;

message = "Transaction complete!" + "\n\n" + "Schedules are split and placed in the following sheets" + "\n\n" + segFinNames + "\n\n" + "Unsplit schedule is placed on the following sheet. Apply manual split if necessary:" + "\n\n" + regFinNames;