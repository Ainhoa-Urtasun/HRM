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
    ### Designing On-the-Job Training
    
    1. Describe what the values on your left represent  
    2. Leverage the visual to provide strong evidence of the expected success of on-the-job training 
    3. Explain the counterfactual skill change, counterfactual skill, and DiD to effectively demonstrate the impact of your training
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
