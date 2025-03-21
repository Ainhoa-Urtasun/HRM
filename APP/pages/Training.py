import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Training():

    with st.sidebar.expander("Skill level of trained employees (Scale: 0-100)"):
        t0 = st.number_input("Before training", key="t0", step=1)
        t1 = st.number_input("After training", key="t1", step=1)
    with st.sidebar.expander("Skill level of non-trained employees' (Scale: 0-100)"):
        n0 = st.number_input("Before training", key="n0", step=1)
        n1 = st.number_input("After training", key="n1", step=1)

    st.write("""
    #### Question 5:
    Fill in the values on your left with made-up data so that the visual demonstrates the effectiveness of the training. Explain what these values mean
    """)
    st.text_area("", placeholder="Writte your response to Question 5 here...") 

    fig = plt.figure(figsize=(5,5),dpi=100)
    plt.plot(['Before training','After training'],[t0,t1],color='red',label="Skill Level of Trained Employees (Scale: 0-100)")
    plt.plot(['Before training','After training'],[n0,n1],color='blue',label="Skill Level of Non-Trained Employees (Scale: 0-100)")
    plt.plot(['Before training','After training'],[t0,t0+(n1-n0)],color='green',ls='-.',label='Counterfactual')
    plt.title('Assessing Training Impact with DiD')
    plt.legend(fontsize=8)
    st.pyplot(fig)

    st.write("""
    #### Question 6:
    Clearly explain the counterfactual skill change, counterfactual skill, and Difference-in-Differences (DiD) values to demonstrate the impact of the training
    """)  
    st.text_area("", placeholder="Writte your response to Question 6 here...") 
  
st.set_page_config(page_title="Training", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['Training'],  # required
    icons=["person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Training":
    Training()
