'use strict'
const { SlayerTool } = require('./modules/SlayerTool.js')

// console.log('SlayerTool: ', SlayerTool);

var x = new SlayerTool()

var Vannaka = new SlayerTool().getVannaka()

console.log(Vannaka.getRandomTask())
