import numpy as np
import json
from numpy.random import choice
import matplotlib.pyplot as plt
plt.rcdefaults()
data_file = "./slayer.json"
increment_file = "./temp.json"

with open(increment_file) as json_file:
    count = json.load(json_file)
count.update({'counter': count['counter']+1})
with open(increment_file, 'w') as outfile:
    json.dump(count, outfile)

with open(data_file) as json_file:
    slayer_data = json.load(json_file)

# Master assignment data initialization
vannaka_assignments = slayer_data['Vannaka']['Assignments']
nieve_assignments = slayer_data['Nieve']['Assignments']
duradel_assignments = slayer_data['Duradel']['Assignments']
krystilia = slayer_data['Krystilia']
chae = slayer_data['Chaelder']
konar = slayer_data['Konar quo Maten']


def test(*args):
    dict_x = slayer_data[args[0]]

    figure_path = './Images/'+args[0]+str(count['counter'])+'.png'
    data_path = './Data/'+args[0]+str(count['counter'])+'.json'
    # Get Total Weight from master
    total_slayer_weight = dict_x['TotalWeight']

    assign_names = []
    weight_array = []
    assign_counter_dict = {}
    sum1 = 0
    for i in dict_x['Assignments']:
        assign_names.append(i)
        print(i, " : ", dict_x['Assignments'][i]['Weight'])
        weight_array.append((dict_x['Assignments'][i]['Weight'] /
                             total_slayer_weight))
        # print(sum(weight_array))
        sum1 = sum1+dict_x['Assignments'][i]['Weight']
        assign_counter_dict.update({i: 0})
    print(sum1)

    # # Creating our data based on our sample size
    sample_size = 100000
    for i in range(0, sample_size):
        rnd = choice(assign_names, p=weight_array)
        assign_counter_dict.update({rnd: assign_counter_dict[rnd]+1})

    # # Initializing graph arrays with x and y columns
    performance = []
    objects = []
    for i in assign_counter_dict:
        print(i, assign_counter_dict[i])
        performance.append(assign_counter_dict[i])
        objects.append(i)

    y_pos = np.arange(len(assign_counter_dict))
    plt.bar(objects, performance, align='center', alpha=0.5, color='red')
    plt.xticks(y_pos, objects, rotation=90, fontsize=6)
    plt.xlabel('Monster')
    plt.title(args[0])
    plt.show()
    plt.savefig(figure_path)
    with open(data_path, 'w') as outfile:
        json.dump(assign_counter_dict, outfile)


test('Konar quo Maten')

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
