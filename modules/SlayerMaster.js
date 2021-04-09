
'use strict';
const { Task } = require('./Task.js')
class SlayerMaster {

    constructor(obj) {
        this.name = obj.name;
        this.tasks = this.generateTasks(obj.tasks);
    }

    generateTasks(tasks) {
        var newTasks = [];

        for (var i in tasks) {
            newTasks.push(new Task(tasks[i]))
        }

        return newTasks;
    }

    /**
    * Get Turael Data
    * @return {Array} Array of tasks for this master class
    * */
    getTasks() {
        return this.tasks;
    }

    /**
     * to string func
     * @todo
     * */
    toString() {
        return 'SlayerMaster :) WIP';
    }



}

module.exports = exports = { SlayerMaster };