// [0] = Cable Tray EE
// [1] = Busduct EE
// [2] = Conduit EE
// [3] = Cable Tray General
// [4] = Ducts General
// [5] = Pipes General
def fieldWidths(x){
WIDTH =
[
[25, 30, 110, 30], //195
[20, 45, 45, 85, 20], //215
[25, 30, 45, 30], //130
[25, 40, 100, 30], //195 
[25, 40, 50, 30], //145
[25, 30, 45, 30] //130
];
return WIDTH[x];
};