allEle;
missingParams;
merged;

errorMessage = "The following parameters are missing:" + "\n\n" + merged;
isEmpty = List.IsEmpty(missingParams);

allowMessage = [Imperative]{
if (isEmpty == true)
	return List.Empty;
else
	return errorMessage;
};

allowToggle = [Imperative]{
	if(isEmpty == true)
		return true;
	else
		return false;
};

allowEle = [Imperative]{
if (isEmpty == true)
	return allEle;
else
	return List.Empty;
};

//output
allowToggle;
allowEle;
"Warning";
allowMessage;