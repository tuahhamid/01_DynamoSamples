linkNames;
validLinks;
toggle;
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
		return toggle;
	else
		return false;
};

allowLinkNames = [Imperative]{
if (isEmpty == true)
	return linkNames;
else
	return List.Empty;
};

allowLinks = [Imperative]{
if (isEmpty == true)
	return validLinks;
else
	return List.Empty;
};

//output
allowLinkNames;
allowLinks;
allowToggle;


"Warning";
allowMessage;