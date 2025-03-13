import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def firm_selection():
    st.write("""
    **Instructions to use SABI (UPNA Library)**:
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

    st.write("""
    ### On-the-Job Training  

    To successfully implement Power BI, employees need specific skills that they may not yet have.  

    #### Step 1: Identify the Key Skill  
    Choose one skill that the on-the-job training should focus on:  
    - **Willingness to learn** – Adapting to new tools and technologies  
    - **Collaboration** – Working effectively in teams and networks  
    - **Efficiency** – Using Power BI to streamline workflows  
    - **Proactive approach** – Taking initiative in data-driven decision-making  

    #### Step 2: Design a Training Program  
    Develop an on-the-job training plan for 'Support intellectuals and scientists, technicians, and professionals' to strengthen the selected skill and ensure a smooth Power BI implementation.  
    """)  

    st.text_area("", placeholder="Write your training plan here.")  

st.set_page_config(page_title="Firm Selection", layout="wide")

selected = option_menu(
    menu_title="",  # No title for the menu
    options=["Firm selection"],  # Menu options
    icons=["book"],  # Icons for options
    menu_icon="cast",  # Icon for the menu
    default_index=0,  # Default selected option
    orientation="vertical",
)

if selected == "Firm selection":
    firm_selection()


