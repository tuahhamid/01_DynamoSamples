// [0] = Cable Tray EE
// [1] = Busduct EE
// [2] = Conduit EE
// [3] = Cable Tray General
// [4] = Ducts General
// [5] = Pipes General

def modFieldName(x)
{
 NAMES =
 [
 [
 "ID NO.",
 "SIZE",
 "CABLE TRAY SYSTEM TYPE",
 "BOT (MSL.)"
 ],
 [
 "ID NO.",
 "SIZE",
 "SYSTEM TYPE",
 "REFERENCE LEVEL",
 "AMP"
 ],
 [
 "ID NO.",
 "SIZE",
 "SYSTEM TYPE",
 "BOC (MSL.)"
 ],
 [
 "ID NO.",
 "SIZE",
 "SYSTEM TYPE",
 "BOT (MSL.)"
 ],
 [
 "ID NO.",
 "SIZE",
 "SYSTEM TYPE",
 "BOD (MSL.)"
 ],
 [
 "ID NO.",
 "SIZE",
 "SYSTEM TYPE",
 "BOP (MSL.)"
 ]
 ];

 return NAMES[x];
};