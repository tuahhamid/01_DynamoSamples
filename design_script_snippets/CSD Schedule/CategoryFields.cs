// [0] = Cable Tray EE
// [1] = Busduct EE
// [2] = Conduit EE
// [3] = Cable Tray General
// [4] = Ducts General
// [5] = Pipes General

def categoryFields(x)
{
 FIELDS =
 	[
 	[
 	"ACM_CSD_Obj ID",
	"Size",
	"Type Mark",
	"ACM_CSD_BotOfEle"
	],
	[
	"ACM_CSD_Obj ID",
	"Size",
	"Type Mark",
	"ACM_CSD_Level Ref",
	"ACM_CSD_Amp Rating"
	],
	[
	"ACM_CSD_Obj ID",
	"Size",
	"Type",
	"ACM_CSD_BotOfEle"
	],
	[
	"ACM_CSD_Obj ID",
	"Size",
	"Type Mark",
	"ACM_CSD_BotOfEle"
	],
	[
	"ACM_CSD_Obj ID",
	"Size",
	"System Abbreviation",
	"ACM_CSD_BotOfEle"
	],
	[
	"ACM_CSD_Obj ID",
	"Size",
	"System Abbreviation",
	"ACM_CSD_BotOfEle"
	]
	];

	return FIELDS[x];
};