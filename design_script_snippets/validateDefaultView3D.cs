document;
userName;

// generate user's 3D view name
userNameView = "{3D - " + userName + "}";

// get active view
activeView = Revit.Document.ActiveView(document);
viewName = Revit.Elements.Element.Name(activeView);

// validate current view is the default 3D view
isValidView = viewName == "{3D}" || viewName == userNameView;

allowView = [Imperative]{
if (isValidView == true)
	return [activeView, true];
else
	return [List.Empty, false];
};

//output
allowView;