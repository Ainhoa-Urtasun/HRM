import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Training():

    with st.sidebar.expander("Skill Level of Trained 'Support intellectuals and scientists, technicians and professionals' (Scale: 0-100)"):
        t0 = st.number_input("Before training", key="t0", step=1)
        t1 = st.number_input("After training", key="t1", step=1)
    with st.sidebar.expander("Skill Level of Non-Trained 'Support intellectuals and scientists, technicians and professionals' (Scale: 0-100)"):
        n0 = st.number_input("Before training", key="n0", step=1)
        n1 = st.number_input("After training", key="n1", step=1)

    st.write("""
    ## On-the-Job Training
    ### 6. Fill in the values on your left and persuasively present your proposed on-the-job training by leveraging the visual to provide compelling evidence of its expected success
    ### 7. Clearly explain the counterfactual skill change, counterfactual skill, and Difference-in-Differences (DiD) values to effectively demonstrate the impact of your training
    """)  

    st.text_area("", placeholder="Writte here...") 
  
    fig = plt.figure(figsize=(5,5),dpi=100)
    plt.plot(['Before training','After training'],[t0,t1],color='red',label="Skill Level of Trained Employees (Scale: 0-100)")
    plt.plot(['Before training','After training'],[n0,n1],color='blue',label="Skill Level of Non-Trained Employees (Scale: 0-100)")
    plt.plot(['Before training','After training'],[t0,t0+(n1-n0)],color='green',ls='-.',label='Counterfactual')
    plt.title('Assessing Training Impact with DiD')
    plt.legend(fontsize=8)
    st.pyplot(fig)
  
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
