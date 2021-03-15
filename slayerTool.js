
import * as slayerData from './data/slayerData.js';
import * as konar from './data/Konar quo Maten.js';
import * as vannaka from './data/Vannaka.js';
import * as nieve from './data/Nieve.js';
import * as mazchna from './data/Mazchna.js';
import * as turael from './data/Turael.js';
import * as krys from './data/Krystilia.js';

export class SlayerTool {
    name = 'SlayerTool'
    osrsAccount = null;
    constructor() {
        this.slayerData = slayerData.default[0];
        this.konarQuoMaten = konar.default[0];
        this.vannaka = vannaka.default[0];
        this.nieve = nieve.default[0];
        this.mazchna = mazchna.default[0];
        this.turael = turael.default[0];
        this.krystilia = krys.default[0];
    }
    /**
     * to string func
     * @todo
     * */
    toString() {
        return 'SlayerTool :) WIP';
    }

    /**
        * Get Turael Data
     * @return {Object} Json data for Turael
         * */
    getTurael() { return this.turael }

    /**
     * Get All Slayer Master Data
     * @return {Object} Json data for all Slayer masters
    * */
    getSlayerData() { return this.slayerData }

    /**
     * Get Vannaka Data
     * @return {Object} Json data for Vannaka
     * */
    getVannaka() { return this.vannaka }

    /**
     * Get Nieve Data
     * @return {Object} Json data for Nieve
     * */
    getNieve() { return this.nieve }

    /**
     * Get Mazchna Data
     * @return {Object} Json data for Mazchna
     * */
    getMaz() { return this.mazchna }
    getMazchna() { return this.mazchna }

    /**
     * Get Krystillia Data
     * @return {Object} Json data for Krystilia
     * */
    getKrystilia() { return this.krystilia }
    getKrys() { return this.krystilia }

    /**
     * Get Konar Data
     * @return {Object} Json data for Konar
     * */
    getKonarQuoMaten() { return this.konarQuoMaten }
    getKonar() { return this.konarQuoMaten }

}

// module.exports = { SlayerTool };
// exports.SlayerTool = SlayerTool;