import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Training():

    with st.sidebar.expander("Skill value (0-10) of the trained 'Support intellectuals and scientists, technicians and professionals'"):
        t0 = st.number_input("Before training", key="t0", step=1)
        t1 = st.number_input("After training", key="t1", step=1)
    with st.sidebar.expander("Skill value (0-100) of the non-trained 'Support intellectuals and scientists, technicians and professionals'"):
        n0 = st.number_input("Before training", key="n0", step=1)
        n1 = st.number_input("After training", key="n1", step=1)

    #### Step 1: Identify the Key Skill  
    Choose one skill, out of the following four, that this on-the-job training should focus on:  
    - **Demonstrating willingness to learn**
    - **Collaborating in teams and networks**
    - **Working efficiently**
    - **Taking a proactive approach**

    #### Step 2: Design a Training Program  
    Develop an on-the-job training plan for 'Support intellectuals and scientists, technicians, and professionals' to strengthen the selected skill and ensure a smooth Power BI implementation.  
    """)  

    st.text_area("", placeholder="Write your training plan here.")  
    fig = plt.figure(figsize=(5,5),dpi=100)
    plt.plot(['-1','+1'],[t0,t1],color='red',label="Trained employee's skill")
    plt.plot(['-1','+1'],[n0,n1],color='blue',label="Non-trained employee's skill")
    plt.plot(['-1','+1'],[t0,t0+(n1-n0)],color='green',ls='-.',label='Counterfactual')
    plt.title('Assessing Training Impact with DiD')
    plt.legend()
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
