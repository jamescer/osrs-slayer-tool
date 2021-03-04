import numpy as np
import json
from numpy.random import choice
import matplotlib.pyplot as plt
import sys
import random
from hiscores import Hiscores
import const
import plotly.express as px
import pandas as pd
from pandas.io.json import json_normalize
plt.rcdefaults()


# author = 'James Cerniglia'

class SlayerTool(object):
    data_file = "./slayer.json"
    account = 0
    username = ''
    combat_level = 0
    count = {}
    slayer_data = {}

    # lets implement quests that can be completedin order to obtain certain tasks
    quests = []

    def __init__(self, **kwargs):
        with open(self.data_file) as json_file:
            self.slayer_data = json.load(json_file)

        self.account = Hiscores(
            kwargs['username']) if 'username' in kwargs.keys() else Hiscores('Lynx Titan')

        self.username = kwargs['username'] if 'username' in kwargs.keys(
        ) else 'Lynx Titan'

        self.combat_level = self.get_cb_lvl()

    # Masters
    masters = {0: "Turael", 1: "Mazchna", 2: "Vannaka", 3: "Chaelder",
               4: "Duradel", 5: "Nieve", 6: "Krystilia", 7: "Konar quo Maten"}

    def set_account(self, x):
        """ 
        Set Acount for object reference, only needed to query once instead of a million times

        Parameters: 
        arg1 (str): Account Name ('Zezima') ('Not Poop')

        Returns: 
        None. Sets this objects self.account object;

        """
        self.account = Hiscores(x)

    def get_doable_assignments(self):
        """ 
        Method that gets all doable assignments based on the account currently tied to this object

        Parameters: 
        None.

        Returns: 
        None. Sets this objects self.account object;

        """
        '''
        
        '''
        doable_tasks = {}
        for m in self.slayer_data:

            # m = master
            doable_tasks[m] = {}
            doable_tasks[m]['assignments'] = {}
            sum1 = 0
            for task in self.slayer_data[m]['assignments']:
                # evaluates task to see if self.account has requirements to do
                addTask = self.evaluate_assignment(self.slayer_data[m], task)

                if addTask:
                    doable_tasks[m]['assignments'].update(
                        {task: self.slayer_data[m]['assignments'][task]})
                    sum1 = sum1 + \
                        self.slayer_data[m]['assignments'][task]['weight']

            doable_tasks[m]['totalWeight'] = sum1

        with open('doable.json', 'w') as outfile:
            json.dump(doable_tasks, outfile)

        return doable_tasks

    def evaluate_assignment(self, Master_dict, assignment):
        '''
        Returns True or False whether the attached account fulfills all the requirements for the said assignment
        Master_dict = [dictionary]: dictionary of the master that has the task being evaluated
        assignment = [string]: name of the monster to be keyed from the dicitionary
        '''
        reqs = Master_dict['assignments'][assignment]
        doable = True
        if 'UnlockRequirements' in Master_dict['assignments'][assignment]:

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
                if i == 'quests':
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

            master_name = kwargs['master_name'] if 'master_name' in kwargs.keys(
            ) and isinstance(kwargs['master_name'], str) else default_master_name
            dict_x = self.slayer_data[kwargs['master_name']
                                      ] if 'master_name' in kwargs.keys() and isinstance(kwargs['master_name'], str) else default_dict_x

            sample_size = kwargs['sample_size'] if 'sample_size' in kwargs.keys(
            ) else default_sample_size
        except Exception as e:
            print("Wrong master")
            return
        # Creating our data based on our sample size

        # Get Total weight from master
        total_slayer_weight = dict_x['totalWeight']

        assign_names = []
        weight_array = []
        assign_counter_dict = {}
        sum1 = 0
        for i in dict_x['assignments']:

            x = self.evaluate_assignment(dict_x, i)

            assign_names.append(i)
            # print(i, " : ", dict_x['assignments'][i]['weight']) # prints the task with the weight.

            weight_array.append((dict_x['assignments'][i]['weight'] /
                                 total_slayer_weight))
            assign_counter_dict.update({i: {'name': i, 'amount': 0}})
            # print(sum(weight_array))
            sum1 = sum1+dict_x['assignments'][i]['weight']

        data_canada = px.data.gapminder().query("country == 'Canada'")

        for i in range(0, sample_size):
            rnd = choice(assign_names, p=weight_array)
            assign_counter_dict[rnd].update(
                {'name': rnd, 'amount': assign_counter_dict[rnd]['amount']+1})

        # # Initializing graph arrays with x and y columns
        performance = [assign_counter_dict[i]['amount']
                       for i in assign_counter_dict]
        objects = [i for i in assign_counter_dict]

        data = {'Name': objects,
                'Times Assigned': performance}

        # Create DataFrame
        df = pd.DataFrame(data)
        fig = px.bar(df, x='Name', y='Times Assigned',
                     color='Times Assigned', title=str(master_name)+", N="+str(sample_size),
                     height=400)
        show_figure = kwargs['show_figure'] if 'show_figure' in kwargs.keys(
        ) else False
        if show_figure:
            fig.show()

    def get_cb_lvl(self):
        x = [0.325*(self.account.skills['attack'].level + self.account.skills['strength'].level), 0.325 *
             (int(3 * self.account.skills['ranged'].level / 2)), 0.325*(int(3 * self.account.skills['magic'].level / 2))]
        x.sort()

        return int(0.25 * (self.account.skills['defence'].level +
                           self.account.skills['hitpoints'].level + (self.account.skills['prayer'].level/2)) + x[-1])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return ' == Slayer Tool Developed by James Cerniglia ==\n Current methods inside of the Slayer Tool \n Current username: '+self.username+'\n Stats: '+str(self.account)


if __name__ == 'main':
    tr = SlayerTool(username='jimbo jango')
    tr.create_graph(master_name='Vannaka', sample_size=1000)
