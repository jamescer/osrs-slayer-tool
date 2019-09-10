import numpy as np
import json
from numpy.random import choice
import matplotlib.pyplot as plt
plt.rcdefaults()
data_file = "./slayer.json"


with open(data_file) as json_file:
    slayer_data = json.load(json_file)

# Master assignment data initialization
vannaka_assignments = slayer_data['Vannaka']['Assignments']
nieve_assignments = slayer_data['Nieve']['Assignments']
duradel_assignments = slayer_data['Duradel']['Assignments']
krystilia_assignments = slayer_data['Krystilia']['Assignments']

# Get Total Weight from master
total_slayer_weight = slayer_data['Krystilia']['TotalWeight']

assign_names = []
weight_array = []
assign_counter_dict = {}

for i in krystilia_assignments:
    assign_names.append(i)
    weight_array.append((krystilia_assignments[i]['Weight'] /
                         total_slayer_weight))
    assign_counter_dict.update({i: 0})

# Creating our data based on our sample size
sample_size = 100000
for i in range(0, sample_size):
    rnd = choice(assign_names, p=weight_array)
    assign_counter_dict.update({rnd: assign_counter_dict[rnd]+1})

# Initializing graph arrays with x and y columns
performance = []
objects = []
for i in assign_counter_dict:
    print(i, assign_counter_dict[i])
    performance.append(assign_counter_dict[i])
    objects.append(i)


y_pos = np.arange(len(assign_counter_dict))
plt.bar(y_pos, performance, align='center', alpha=0.5, color='red')
plt.xticks(y_pos, objects, rotation=90, fontsize=6)
plt.xlabel('Monster')
plt.title('Task amounts')
plt.show()
plt.figure().savefig('temp.png', dpi=plt.figure().dpi)
plt.savefig("./Images/Krystilia.png")
with open('./Data/Krystilia.json', 'w') as outfile:
    json.dump(assign_counter_dict, outfile)
