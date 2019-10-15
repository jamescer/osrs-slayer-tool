import numpy as np
import json
from numpy.random import choice
import matplotlib.pyplot as plt
import sys
import random
from hiscores import Hiscores
from colorama import init, Fore, Back, Style
init(autoreset=True)
plt.rcdefaults()
author = 'James Cerniglia'

# Runtime Execution
# slayer.py 'slayer_master' 'sample_size'


class SlayerTool(object):
    data_file = "./slayer.json"
    increment_file = "./counter.json"
    account = 0
    combat_level = 0

    with open(data_file) as json_file:
        slayer_data = json.load(json_file)

    def __init__(self, *args):
        if len(args) > 1:
            self.account = Hiscores(args[0])
            self.combat_level = self.get_cb_lvl(self.account)
        else:
            self.account = Hiscores('Lynx Titan')
            self.combat_level = self.get_cb_lvl(self.account)
        # Counter File for incrementation
        with open(self.increment_file) as json_file:
            self.count = json.load(json_file)
        self.count.update({'counter': self.count['counter']+1})

        with open(self.increment_file, 'w') as outfile:
            json.dump(self.count, outfile)

    # Masters
    masters = {0: "Turael", 1: "Mazchna", 2: "Vannaka", 3: "Chaelder",
               4: "Duradel", 5: "Nieve", 6: "Krystilia", 7: "Konar quo Maten"}

    # Master assignment data initialization
    vannaka_assignments = slayer_data['Vannaka']
    nieve_assignments = slayer_data['Nieve']
    duradel_assignments = slayer_data['Duradel']
    krystilia = slayer_data['Krystilia']
    chaelder = slayer_data['Chaelder']
    konar = slayer_data['Konar quo Maten']
    turael = slayer_data['Turael']

    def set_account(self, x):
        '''
        Set Acount for object reference, only needed to query once instead of a million times
        '''
        self.account = Hiscores(x)

    def reset_counter(self):
        '''
        Reset counter for file outputs
        '''
        self.count = 0
        with open(self.increment_file, 'w') as outfile:
            json.dump(self.count, outfile)

    def get_doable_assignments(self, input_slayer_level):
        doable_tasks = {}
        for m in slayer_data:
            # m = master
            doable_tasks[m] = {}
            doable_tasks[m]['Assignments'] = {}
            sum1 = 0
            for t in slayer_data[m]['Assignments'].items():
                # t= task
                addTask = True
                if 'UnlockRequirements' in slayer_data[m]['Assignments'][t[0]]:
                    if 'Slayer' in slayer_data[m]['Assignments'][t[0]]['UnlockRequirements']:
                        if account.skills['slayer'].level >= slayer_data[m]['Assignments'][t[0]]['UnlockRequirements']['Slayer']:
                            print('higher : ', account.skills['slayer'].level, ' vs ',
                                  slayer_data[m]['Assignments'][t[0]]['UnlockRequirements']['Slayer'])
                            addTask = True
                        else:
                            addTask = False
                    if 'Combat' in slayer_data[m]['Assignments'][t[0]]['UnlockRequirements']:
                        if account.combat >= slayer_data[m]['Assignments'][t[0]]['UnlockRequirements']['Slayer']:
                            addTask = True
                        else:
                            addTask = False
                else:
                    print('no requirements for task:', t[0])

                if addTask:
                    doable_tasks[m]['Assignments'].update({t[0]: t[1]})
                    sum1 = sum1+slayer_data[m]['Assignments'][t[0]]['Weight']

            doable_tasks[m]['TotalWeight'] = sum1

        with open('doable.json', 'w') as outfile:
            json.dump(doable_tasks, outfile)

    def evaluate_assignment(self, dict_x, assignment):

        if 'UnlockRequirements' in dict_x['Assignments'][assignment]:
            print(dict_x['Assignments'][assignment]['UnlockRequirements'])
            for i in dict_x['Assignments'][assignment]['UnlockRequirements']:
                if i == 'Slayer':
                    if self.account.skills['slayer'].level >= dict_x['Assignments'][assignment]['UnlockRequirements']['Slayer']:
                        doable = True
                    else:
                        doable = False
                if i == 'Combat':
                    if self.combat_level >= dict_x['Assignments'][assignment]['UnlockRequirements']['Combat']:
                        doable = True
                    else:
                        doable = False
                if i != 'or' or 'Combat' or 'Quests' or 'partialQuests':
                    # any skill but those
                    todo=0
                if i == 'Quests':
                    # TODO
                    have_not_implemented_quest_checking=0
                if i == 'partialQuests':
                     # TODO
                    have_not_implemented_quest_checking=0
        else:  # Krystilia else statement, none of her tasks have requirements.
            var = 0

    def create_graph(self, *args):
        '''
        Creates graph based on input variables
        args[0] = Slayer master ('0' or 'Vannaka')          default: random
        args[1] = sample size                               default: 1000
        args[2] = username or level ('jimbo jango' or '65') default: 99
        '''

        master_name = self.masters.get(random.randint(
            0, len(self.masters)-1), "Please either use the name of the master or an integer from the dictionary"+str(self.masters))
        dict_x = self.slayer_data[master_name]
        sample_size = 1000
        if len(args) > 0:
            # can either use "0" for Tureal or 'Vannaka' for respected slayer master

            if isinstance(args[0], str):
                master_name = args[0]
                dict_x = self.slayer_data[args[0]]

            elif isinstance(args[0], int):
                master_name = self.masters.get(int(
                    args[0]), "Please either use the name of the master or an integer from the dictionary : "+str(self.masters))
                dict_x = self.slayer_data[master_name]

            # Default sample size is 1000 but they can set it with one more number
            if len(args) > 1:
                if isinstance(args[2], int):
                    sample_size = int(args[1])

        # Creating our data based on our sample size

        # Paths for saving data
        figure_path = './Images/'+master_name+str(self.count['counter'])+'.png'
        data_path = './Data/'+master_name+str(self.count['counter'])+'.json'

        # Get Total Weight from master
        total_slayer_weight = dict_x['TotalWeight']

        assign_names = []
        weight_array = []
        assign_counter_dict = {}
        sum1 = 0
        for i in dict_x['Assignments']:

            x = self.evaluate_assignment(dict_x, i)
            print(x)
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
        plt.bar(objects, performance, align='center', alpha=0.5, color='red')
        plt.xticks(y_pos, objects, rotation=90, fontsize=6)
        plt.xlabel('Monster')
        plt.title(master_name)
        plt.show()
        plt.savefig(figure_path)

        # Saves data to a json if the user wants to see the data and use it for something else.
        with open(data_path, 'w') as outfile:
            json.dump(assign_counter_dict, outfile)

    def get_cb_lvl(self, acc):
        x = [0.325*(acc.skills['attack'].level + acc.skills['strength'].level), 0.325 *
             (int(3 * acc.skills['ranged'].level / 2)), 0.325*(int(3 * acc.skills['magic'].level / 2))]
        x.sort()

        return int(0.25 * (acc.skills['defence'].level +
                           acc.skills['hitpoints'].level + (acc.skills['prayer'].level/2)) + x[-1])

    def get_help(self):
        print(Fore.CYAN+'    == Current List of implemented commands ==')
        print(Fore.BLUE + '\"-doable\"'+Fore.GREEN +
              '     - Gets all the doable tasks at your current slayer level')
        print(Fore.BLUE + '\"-g\"'+Fore.GREEN +
              '          - Generates graphs based on tasks you\'re available to get')
        print(Fore.BLUE + '\"-g -nolimit\"'+Fore.GREEN +
              ' - Generates graphs at level 99 slayer all quests unlocked')
        print(Fore.BLUE + '\"-doable\"'+Fore.GREEN +
              '     - Gets all the doable tasks at your current slayer level')

    def __str__(self):
        global author
        stringify = ' == Slayer Tool Developed by '+author+' ==\n \
                    Current methods inside of the Slayer Tool'
        return super().__str__()
    if len(sys.argv) > 1:
        start(sys.argv[1:])
    else:
        print(Fore.GREEN+'No command line arguments given, try:')
        print('py slayer.py '+Fore.BLUE+'\"user_name\" (use _ for spaces) '+Fore.RED+'\"command\" ' +
              Fore.WHITE+'- '+Fore.YELLOW+'Need help? do  py slayer.py -cmd')
