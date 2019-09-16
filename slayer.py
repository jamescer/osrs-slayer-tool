import numpy as np
import json
from numpy.random import choice
import matplotlib.pyplot as plt
import sys
import random
print(sys.argv)

plt.rcdefaults()
data_file = "./slayer.json"
increment_file = "./counter.json"

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
masters = {0: "Tureal",
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

# Runtime Execution
# slayer.py 'slayer_master' 'sample_size'


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
    print(args)
    args = args[0]

    random_master = random.randint(0, 7)
    master_name = masters.get(random_master, "Invalid Number")
    dict_x = slayer_data[master_name]
    sample_size = 10000

    if len(args) > 0:
        master_name = masters.get(int(args[0]), "Invalid Number")
        dict_x = slayer_data[master_name]
        sample_size = 10000
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


test(sys.argv[1:])

# for j in slayer_data:
#     # for h in i['Assignments']:
#     #     var=0
#     print(j+": "+str(len(slayer_data[j]['Assignments'])))
#     assign_names = []
#     weight_array = []
#     assign_counter_dict = {}
#     for l in slayer_data[j]['Assignments']:
#         assign_names.append(l)
#         weight_array.append((slayer_data[j]['Assignments'][l]['Weight'] /
#                             slayer_data[j]['TotalWeight']))
#         assign_counter_dict.update({l: 0})
#     sample_size = 100000
#     for k in range(0, sample_size):
#         rnd = choice(assign_names, p=weight_array)
#         assign_counter_dict.update({rnd: assign_counter_dict[rnd]+1})
#     performance = []
#     objects = []
#     for m in assign_counter_dict:
#         print(m, assign_counter_dict[m])
#         performance.append(assign_counter_dict[m])
#         objects.append(m)
#     y_pos = np.arange(len(assign_counter_dict))
#     plt.bar(y_pos, performance, align='center', alpha=0.5, color='red')
#     plt.xticks(y_pos, objects, rotation=90, fontsize=6)
#     plt.xlabel('Assignment')
#     plt.ylabel('Amount of Assignments')
#     plt.title(j)

#     plt.show()
#     with open('./Data/'+j+'.json', 'w') as outfile:
#         json.dump(assign_counter_dict, outfile)
