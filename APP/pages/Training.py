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

    st.write("""
    ### Instructions to use SABI (UPNA Library):
    1. In **Personalizar** -> **Opciones generales**, set **Idioma** to English.
    2. In **Employees** -> **Employees' segmentation in Spain**:
       - In **Type of employee**, select:
         - Other managers
         - Support intellectuals and scientists, technicians and professionals
         - Administrative employees
       - In **Select periods** -> **Absolute years**, select **2022** and **2023**
       - In **Criteria to be valid**, ensure **All selected years** is chosen
       - In **Select the gender**, set a minimum of **250 Women**
    3. Choose **one firm** from the resulting firms
    """)
    st.text_area("", placeholder="Type the name of your firm, NACE Rev. 2 Primary Code, and English trade description")
    st.text_area("", placeholder="The firm is about to implement Power BI. Explain how Power BI can benefit your company.")  
  

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
