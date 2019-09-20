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
data_file = "./slayer.json"
increment_file = "./counter.json"
account = 0

# Counter File for incrementation
with open(increment_file) as json_file:
    count = json.load(json_file)
count.update({'counter': count['counter']+1})

with open(increment_file, 'w') as outfile:
    json.dump(count, outfile)

# Slayer file
with open(data_file) as json_file:
    slayer_data = json.load(json_file)

# Masters
masters = {0: "Turael",
           1: "Mazchna",
           2: "Vannaka",
           3: "Chaelder",
           4: "Duradel",
           5: "Nieve",
           6: "Krystilia",
           7: "Konar quo Maten"
           }

# Master assignment data initialization
vannaka_assignments = slayer_data['Vannaka']['Assignments']
nieve_assignments = slayer_data['Nieve']['Assignments']
duradel_assignments = slayer_data['Duradel']['Assignments']
krystilia = slayer_data['Krystilia']
chae = slayer_data['Chaelder']
konar = slayer_data['Konar quo Maten']
turael = slayer_data['Turael']
# Runtime Execution
# slayer.py 'slayer_master' 'sample_size'


def get_doable_assignments(input_slayer_level):
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


def evaluate_assignment(dict_x):
    for i in dict_x['Assignments']:
        print('==', i, '==')
        if 'UnlockRequirements' in dict_x['Assignments'][i]:
            for i in dict_x['Assignments'][i]['UnlockRequirements']:
                if i == 'Slayer':
                    var = 0
                if i == 'Combat':
                    var = 0
                if i == 'Quests':
                    var = 0
                if i == 'partialQuests':
                    var = 0
        else:  # Krystilia else statement, none of her tasks have requirements.
            var = 0


def test(*args):

    args = args[0]
    random_master = random.randint(0, 7)
    master_name = masters.get(random_master, "Indoable Number")
    dict_x = slayer_data[master_name]
    sample_size = 10000

    if len(args) > 0:
        master_name = masters.get(int(args[0]), "Indoable Number")
        dict_x = slayer_data[master_name]

        if len(args) > 1:
            sample_size = int(args[1])

    # Creating our data based on our sample size

    # Paths for saving data
    figure_path = './Images/'+master_name+str(count['counter'])+'.png'
    data_path = './Data/'+master_name+str(count['counter'])+'.json'

    # Get Total Weight from master
    total_slayer_weight = dict_x['TotalWeight']

    assign_names = []
    weight_array = []
    assign_counter_dict = {}
    sum1 = 0
    for i in dict_x['Assignments']:
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


# test(sys.argv[1:])


def get_cb_lvl(acc):
    x = [0.325*(acc.skills['attack'].level + acc.skills['strength'].level), 0.325 *
         (int(3 * acc.skills['ranged'].level / 2)), 0.325*(int(3 * acc.skills['magic'].level / 2))]
    x.sort()

    return int(0.25 * (acc.skills['defence'].level +
                       acc.skills['hitpoints'].level + (acc.skills['prayer'].level/2)) + x[-1])


def get_help():
    print(Fore.CYAN+'    == Current List of implemented commands ==')
    print(Fore.BLUE + '\"-doable\"'+Fore.GREEN +
          '     - Gets all the doable tasks at your current slayer level')
    print(Fore.BLUE + '\"-g\"'+Fore.GREEN +
          '          - Generates graphs based on tasks you\'re available to get')
    print(Fore.BLUE + '\"-g -nolimit\"'+Fore.GREEN +
          ' - Generates graphs at level 99 slayer all quests unlocked')
    print(Fore.BLUE + '\"-doable\"'+Fore.GREEN +
          '     - Gets all the doable tasks at your current slayer level')


def start(arr):
    if len(arr) >= 1:
        command = arr[0]
        if command == '-cmd':
            get_help()
        else:
            ACCOUNT = arr[0].replace('_', ' ')
            global account
            account = Hiscores(ACCOUNT)
            account.combat = get_cb_lvl(account)
        


if len(sys.argv) > 1:
    start(sys.argv[1:])
else:
    print(Fore.GREEN+'No command line arguments given, try:')
    print('py slayer.py '+Fore.BLUE+'\"user_name\" (use _ for spaces) '+Fore.RED+'\"command\" ' +
          Fore.WHITE+'- '+Fore.YELLOW+'Need help? do  py slayer.py -cmd')
