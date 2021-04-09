import json
slayer_data = {}


def add_amount_numbers():
    # get json data
    with open("./slayer.json") as json_file:
        slayer_data = json.load(json_file)
    # new dict to create
    newDict = {}
    for i in slayer_data.keys():
        newDict[i] = {'name': i, 'assignments': []}
        for x in slayer_data[i].keys():

            newDict[i][x] = slayer_data[i][x]
        tasks = slayer_data[i]['assignments']

        tasksArr = []
        for j in tasks:
            appendDict = {'name': j}
            for z in tasks[j].keys():
                if z == 'amount':
                    splt = tasks[j][z].split('-')
                    appendDict['amountMin'] = int(splt[0])
                    if len(splt) > 1:
                        appendDict['amountMax'] = int(splt[1])
                    else:
                        appendDict['amountMax'] = int(splt[0])
                elif z == 'extendedAmount' and tasks[j][z] != None:
                    splt = tasks[j][z].split('-')
                    appendDict['extendedAmountMin'] = int(splt[0])
                    if len(splt) > 1:
                        appendDict['extendedAmountMax'] = int(splt[1])
                    else:
                        appendDict['extendedAmountMax'] = int(splt[0])
                elif z == 'extendedAmount' and tasks[j][z] == None:
                    appendDict['extendedAmountMin'] = None
                    appendDict['extendedAmountMax'] = None
                else:
                    appendDict[z] = tasks[j][z]
            tasksArr.append(appendDict)
        newDict[i]['assignments'] = tasksArr

    with open('./slayerData.json', 'w') as outfile:
        json.dump(newDict, outfile)
