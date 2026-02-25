input;
wasRun;
wasCancelled;

isEmpty = List.IsEmpty(input);
checkNulls = input == null;
isNull = List.AnyTrue(checkNulls);

allowInput = [Imperative]{
if (wasCancelled == true)
	return List.Empty;
if (wasRun == true && isEmpty == false)
	return input[0];
};

isEmptyOutput = List.IsEmpty(allowInput);
allowToggle = [Imperative]{
if (isEmptyOutput == true)
	return false;
else
	return true;
};

//output
allowInput;
allowToggle;