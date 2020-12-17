
"use strict";

let LoadExternalMap = require('./LoadExternalMap.js')
let DeleteSoundSource = require('./DeleteSoundSource.js')
let AddRfidTag = require('./AddRfidTag.js')
let DeleteRfidTag = require('./DeleteRfidTag.js')
let LoadMap = require('./LoadMap.js')
let AddSoundSource = require('./AddSoundSource.js')
let AddThermalSource = require('./AddThermalSource.js')
let DeleteCO2Source = require('./DeleteCO2Source.js')
let AddCO2Source = require('./AddCO2Source.js')
let MoveRobot = require('./MoveRobot.js')
let RegisterGui = require('./RegisterGui.js')
let DeleteThermalSource = require('./DeleteThermalSource.js')

module.exports = {
  LoadExternalMap: LoadExternalMap,
  DeleteSoundSource: DeleteSoundSource,
  AddRfidTag: AddRfidTag,
  DeleteRfidTag: DeleteRfidTag,
  LoadMap: LoadMap,
  AddSoundSource: AddSoundSource,
  AddThermalSource: AddThermalSource,
  DeleteCO2Source: DeleteCO2Source,
  AddCO2Source: AddCO2Source,
  MoveRobot: MoveRobot,
  RegisterGui: RegisterGui,
  DeleteThermalSource: DeleteThermalSource,
};
