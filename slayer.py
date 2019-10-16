import numpy as np
import json
from numpy.random import choice
import matplotlib.pyplot as plt
import sys
import random
from hiscores import Hiscores
from colorama import init, Fore, Back, Style
import const
init(autoreset=True)
plt.rcdefaults()
author = 'James Cerniglia'

# Runtime Execution
# slayer.py 'slayer_master' 'sample_size'


class SlayerTool(object):
    data_file = "./slayer.json"
    increment_file = "./counter.json"
    account = 0
    username = ''
    combat_level = 0
    count = {}
    slayer_data = {}

    def __init__(self, **kwargs):
        with open(self.data_file) as json_file:
            self.slayer_data = json.load(json_file)

        self.account = Hiscores(
            kwargs['username']) if 'username' in kwargs.keys() else Hiscores('Lynx Titan')

        self.username = kwargs['username'] if 'username' in kwargs.keys(
        ) else 'Lynx Titan'

        self.combat_level = self.get_cb_lvl()

        # Counter File for incrementation
        with open(self.increment_file) as json_file:
            self.count = json.load(json_file)
        self.count.update({'counter': self.count['counter']+1})

        with open(self.increment_file, 'w') as outfile:
            json.dump(self.count, outfile)

    # Masters
    masters = {0: "Turael", 1: "Mazchna", 2: "Vannaka", 3: "Chaelder",
               4: "Duradel", 5: "Nieve", 6: "Krystilia", 7: "Konar quo Maten"}

    def set_account(self, x):
        '''
        Set Acount for object reference, only needed to query once instead of a million times
        '''
        self.account = Hiscores(x)

    def reset_counter(self):
        '''
        Reset counter for file outputs
        '''
        self.count.update({'counter': 0})
        with open(self.increment_file, 'w') as outfile:
            json.dump(self.count, outfile)

    def get_doable_assignments(self):
        '''
        Method that gets all doable assignments based on the account currently tied to this object
        '''
        doable_tasks = {}
        for m in self.slayer_data:

            # m = master
            doable_tasks[m] = {}
            doable_tasks[m]['Assignments'] = {}
            sum1 = 0
            for task in self.slayer_data[m]['Assignments']:
                # evaluates task to see if self.account has requirements to do
                addTask = self.evaluate_assignment(
                    self.slayer_data[m], task)

                if addTask:
                    doable_tasks[m]['Assignments'].update(
                        {task: self.slayer_data[m]['Assignments'][task]})
                    sum1 = sum1 + \
                        self.slayer_data[m]['Assignments'][task]['Weight']

            doable_tasks[m]['TotalWeight'] = sum1

        with open('doable.json', 'w') as outfile:
            json.dump(doable_tasks, outfile)

    def evaluate_assignment(self, Master_dict, assignment):
        '''
        Returns True or False whether the attached account fulfills all the requirements for the said assignment
        Master_dict = [dictionary]: dictionary of the master that has the task being evaluated
        assignment = [string]: name of the monster to be keyed from the dicitionary
        '''
        reqs = Master_dict['Assignments'][assignment]
        doable = True
        if 'UnlockRequirements' in Master_dict['Assignments'][assignment]:

            doable = True
            for i in reqs['UnlockRequirements']:
                if i == 'Combat':
                    if self.combat_level < reqs['UnlockRequirements']['Combat']:
                        doable = False
                if i.lower() in const.SKILLS:
                    # any skill inside const.SKILLS array
                    if self.account.skills[i.lower()].level < reqs['UnlockRequirements'][i]:
                        doable = False
                # These are the conditional outliers I have not implemented
                if i == 'or':
                    # TODO
                    have_not_implemented = 0
                if i == 'SlayerRewards':
                    # TODO
                    have_not_implemented = 0
                if i == 'MiniQuests':
                    # TODO
                    have_not_implemented = 0
                if i == 'Favor':
                    # TODO
                    have_not_implemented = 0
                if i == 'Quests':
                    # TODO
                    have_not_implemented = 0
                if i == 'partialQuests':
                    # TODO
                    have_not_implemented = 0
            return doable
        else:  # Krystilia else statement, none of her tasks have requirements.
            var = 0
            return doable

    def create_graph(self, **kwargs):
        '''
        Creates graph based on input variables
        args[0] = Slayer master ('0' or 'Vannaka')          default: random
        args[1] = sample size                               default: 1000
        args[2] = username or level ('jimbo jango' or '65') default: 99
        '''
        try:
            default_sample_size = 1000
            default_master_name = self.masters.get(random.randint(
                0, len(self.masters)-1), "Please either use the name of the master or an integer from the dictionary"+str(self.masters))
            default_dict_x = self.slayer_data[default_master_name]

            master_name = kwargs['master_name'] if 'master_name'in kwargs.keys(
            ) and isinstance(kwargs['master_name'], str) else default_master_name
            dict_x = self.slayer_data[kwargs['master_name']
                                      ] if 'master_name'in kwargs.keys() and isinstance(kwargs['master_name'], str) else default_dict_x
            sample_size = kwargs['sample_size'] if 'sample_size' in kwargs.keys(
            ) else default_sample_size
        except Exception as e:
            print("Wrong master")
            return
        # Creating our data based on our sample size

        # Get Total Weight from master
        total_slayer_weight = dict_x['TotalWeight']

        assign_names = []
        weight_array = []
        assign_counter_dict = {}
        sum1 = 0
        for i in dict_x['Assignments']:

            x = self.evaluate_assignment(dict_x, i)

            assign_names.append(i)
            # print(i, " : ", dict_x['Assignments'][i]['Weight']) # prints the task with the weight.

            weight_array.append((dict_x['Assignments'][i]['Weight'] /
                                 total_slayer_weight))
            assign_counter_dict.update({i: 0})
            # print(sum(weight_array))
            sum1 = sum1+dict_x['Assignments'][i]['Weight']

        # print(sum1)# prints the sum of all the weights, should always be equal to the masters total weight.

        for i in range(0, sample_size):
            rnd = choice(assign_names, p=weight_array)
            assign_counter_dict.update({rnd: assign_counter_dict[rnd]+1})

        # # Initializing graph arrays with x and y columns
        performance = []
        objects = []

        for i in assign_counter_dict:
            # print(i, assign_counter_dict[i]) #prints the assignment ant how many times it was chosen while adding everything to 2 data arrays
            performance.append(assign_counter_dict[i])
            objects.append(i)


        # Creating actual figure
        y_pos = np.arange(len(assign_counter_dict))
        plt.bar(objects, performance, align='center',
                alpha=0.5, color='red')
        plt.xticks(y_pos, objects, rotation=90, fontsize=6)
        plt.xlabel('Monster')
        plt.title(master_name)
        # plt.show()
        plt.savefig('./Images/'+master_name + \
            str(self.count['counter'])+'.png')

        # Saves data to a json if the user wants to see the data and use it for something else.
        with open('./Data/'+master_name + \
            str(self.count['counter'])+'.json', 'w') as outfile:
            json.dump(assign_counter_dict, outfile)

    def get_cb_lvl(self):
        x = [0.325*(self.account.skills['attack'].level + self.account.skills['strength'].level), 0.325 *
             (int(3 * self.account.skills['ranged'].level / 2)), 0.325*(int(3 * self.account.skills['magic'].level / 2))]
        x.sort()

        return int(0.25 * (self.account.skills['defence'].level +
                           self.account.skills['hitpoints'].level + (self.account.skills['prayer'].level/2)) + x[-1])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        global author

        return ' == Slayer Tool Developed by '+author+' ==\n Current methods inside of the Slayer Tool \n Current username: '+self.username+'\n Stats: '+str(self.account)
