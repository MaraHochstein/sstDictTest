#######################
# imports & cofig
#######################
# imports
from utils.imports import (st, sst, pd)
import utils.func as fn


#######################
# vars
#######################

hasdict1data = [True, True, False]
dict1data1 = [[['Name', 'Emily'], ['Age', '40']], [['Name', 'Alan'], ['Age', '25']], []]
dict1data2 = [[['Name', 'Emily'], ['Gender', 'Female']], [], [['Name', 'Alan'], ['Gender', 'Male']]]

dataID = [['abc1','def1','ghi1'], ['abc2','def2','ghi2'], ['abc3','def3','ghi3']]
dict2data = [{123:'img name one1', 321:'img name two1', 231:'img name three1'}, {985:'img name one2', 598:'img name two2', 895:'img name three2'}, {764:'img name one3', 674:'img name two3', 476:'img name three3'}]



########################
# import
########################
def importData(selectedDataset):
    sstVars = ['strVar','boolVar', 'dfVar', 'listVar', 'dictVar1', 'dictVar2']
    
    for var in sstVars:
        fn.resetVar(var)
    
    # bool var example
    sst.boolVar = hasdict1data[selectedDataset]
    
    # df var example
    sst.dfVar = pd.DataFrame(dict1data1[selectedDataset])
    
    # str var example
    sst.strVar = dataID[selectedDataset][0]

    # list var example
    sst.listVar = dataID[selectedDataset]
    
    # dict 1 example
    if hasdict1data[selectedDataset]:
        #sst.dictVar1 = {}
        sst.dictVar1[0] = dict1data1[selectedDataset]
        sst.dictVar1[1] = dict1data2[selectedDataset]
    
    # dict 2 example
    #sst.dictVar2 = {}
    for img in dict2data[selectedDataset].keys():
        strings = dict2data[selectedDataset][img].split(' ')
        sst.dictVar2[img] = {'string1': strings[0],
                            'string2': strings[1],
                            'string3': strings[2]
                            }