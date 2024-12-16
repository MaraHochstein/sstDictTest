#######################
# imports
#######################
from utils.imports import (st, sst, pd, copy)

#######################
# variables
#######################
global variableList
variableList = [    
    # record variables
    ['dontDelete', ''],
    ['listVar', []],
    ['strVar', ''],
    ['boolVar', False],
    ['dfVar', pd.DataFrame()],
    ['dictVar1', dict()],
    ['dictVar2', {}]
]


#####################
# session_state
#####################
# set up session_state
def initSessionState():
    for variable in variableList:
        saveVar(variable[0], variable[1])

# save var in session_state
def saveVar(variableName, variable):
    if variableName not in sst:
        sst[variableName] = copy.deepcopy(variable)
    
# reset session_state
def deleteSessionState():
    st.divider()
    st.header('showing sst while deleteSessionState()')
    # delete all except auth variables
    keysDelete = [string for string in sst.keys() if string not in ['dontDelete']]
    for key in keysDelete:
        del sst[key]
    st.info('deleted')
    showSessionState()
    initSessionState()
    st.info('initialized')
    showSessionState()
    st.divider()
    
# reset one session_state variable
def resetVar(variableName):
    sst[variableName] = [variable[1] for variable in variableList if variable[0] == variableName][0]

# show session_state
def showSessionState():
    st.subheader('session_state')
    st.write(sst)