// ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╦  
// ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣║  
// ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩╩═╝

// <summary>
// This code calculates the required number of schedules based on the maximum element count per sheet for cable trays and ducts.
// The calculations are done for different model codes (EE, ECS, SN, FP, TV) which represent different systems in the project.
// Current unmodifieable schedule apperance values are below
// ColumnHeaderHeight = 0.0220095656008726ft (6.7085156mm)
// TitleHeight = 0.0347222222222222ft (10.5833333mm)
// RowHeight = 0.0188653419436051ft (5.7500000mm)
// API's GetSegmentHeight = Actual ScheduleInstance Height - ColumnHeaderHeight - TitleHeight - RowHeight (for each row)
// For example, Actual = 511.8mm
// API's GetSegmentHeight = 511.8mm - 6.7085156mm = 505mm ish
// </summary>

//calculate schedule required
//assume 164 elements per sheet for cable tray
ctScheduleMax = DSCore.Math.Ceiling(allowCounts/246);

//calculate schedule required
//assume 328 elements per sheet for ducts
ductScheduleMax = DSCore.Math.Ceiling(allowCounts/328);

//calculate schedule required
//assume 328 elements per sheet for pipes
pipeScheduleMax = DSCore.Math.Ceiling(allowCounts/328);

// ╔═╗╦  ╔═╗╔═╗╔╦╗╦═╗╦╔═╗╔═╗╦  
// ║╣ ║  ║╣ ║   ║ ╠╦╝║║  ╠═╣║  
// ╚═╝╩═╝╚═╝╚═╝ ╩ ╩╚═╩╚═╝╩ ╩╩═╝

//calculate schedule required
//assume 164 element per sheet for cable tray
ctScheduleMaxEE = DSCore.Math.Ceiling(allowCounts/246);

//calculate schedule required
//assume 328 element per sheet for ducts
ductScheduleMaxEE = DSCore.Math.Ceiling(allowCounts/328);

//calculate schedule required
//assume 328 element per sheet for pipes
pipeScheduleMaxEE = DSCore.Math.Ceiling(allowCounts/328);

//calculate schedule required
//assume 328 element per sheet for conduits
conduitScheduleMaxEE = DSCore.Math.Ceiling(allowCounts/328);