import streamlit as st
import pandas as pd
import numpy as np
import streamlit_modal as modal
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
 


open_modal = st.button("Login")
if open_modal:
    modal.open()

if modal.is_open():
    
    with modal.container():
                title_1 = st.text_input("User ",'User name')
                title = st.text_input("Password",'Password', type="password")
                
                st.button("se connecter")
                st.button("Mot de passe oublier")

                
col1, col2 = st.columns([5, 2])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)












###### clée et valeur ##########
st.write("a_counter is : ", st.session_state['a_counter'])
st.write("boolean is : ", st.session_state.boolean)
###### afficher les clées ###########
for the_key in st.session_state.keys():
    st.write(the_key)
########afficher les valeur ########
for the_values in st.session_state.values():
    st.write(the_values)
  ###########pourafficher les items (keys , value)
for item in st.session_state.items():
    item
######### Mettre à jour l a session_state ###########
button = st.button("Update state")
"befor pressing button" , st.session_state
if button:
    st.session_state['a_counter'] +=1
    st.session_state.boolean = not st.session_state.boolean
    "after pressing button",st.session_state
######### effacer une session_state ###########
button_1 = st.button("delete state")
if button_1 :
    for key in st.session_state.keys():
        del st.session_state[key]
st.session_state
###############session_state sur un widget ###############
"session_state avec les widgets"

number = st.slider("A number",5,10) ############ la clée ajouté est "slider" ###########
st.write(number)
st.session_state.slider= number
st.write(st.session_state)
############## avec les cases ###############
col1,buff,col2 = st.columns(([1,0.5,3]))
option_names = ["a" , "b" , "c"]
  ########## bouton pour faire le choix automatiquement ########
next = st.button("Next option")
if next:
    if st.session_state["radio_option"] == 'a':
        st.session_state.radio_option = 'b'
    elif st.session_state["radio_option"] == 'b':
        st.session_state.radio_option = 'c'
    else:
        st.session_state.radio_option = 'a'
  ##########################################
option = col1.radio("pick an option",option_names,key="radio_option")

if option == 'a':
    col2.write("You picked 'a' : smile:")
elif option == "b":
    col2.write("you picked 'b' :heart:")
elif option == "c":
    col2.write("you puicked 'c' :rocket:")
st.session_state
################ How callbacks work ? ############
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
####################