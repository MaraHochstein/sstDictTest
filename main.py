#######################
# imports & cofig
#######################
# imports
from utils.imports import (st, sst, pd)
import utils.func as fn
from utils.importFunctions import (importData)

# set up variables in session_state
fn.initSessionState()

#page config
st.set_page_config(page_title='Testing', layout='wide', initial_sidebar_state='expanded')


#########################
# welcome page
#########################  
st.title('Testing')

if sst.strVar == '':
    st.subheader('Load data', anchor=False)
    
    left, mid, right = st.columns(3)
    
    with left:
        st.button('first dataset', type='primary', on_click=lambda:importData(0))
        
    with mid:
        st.button('second dataset', type='primary', on_click=lambda:importData(1))
        
    with right:
        st.button('third dataset (has no dict1 entries)', type='primary', on_click=lambda:importData(2))
 
else:
    st.subheader('Delete data', anchor=False)
    
    st.button('Delete sst', type='primary', on_click=fn.deleteSessionState)

st.divider()
fn.showSessionState()