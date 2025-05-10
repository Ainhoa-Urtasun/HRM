import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def firm_selection():
    st.write("""
    ## Instructions to use SABI (UPNA Library):
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

    st.write("""
    #### Question 1: 
    At the end of 2023, your firm promoted 1 woman and 1 man from the job category 'Support Intellectuals and Scientists, Technicians, and 
    Professionals' to 'Other Managers'. Additionally, during 2023, 2 women and 3 men from this job left the firm. Assume
    there were no other workforce movements.
    1. Calculate the turnover rate for this job category by gender.
    2. Explain the formula you used for the calculation.
    """)
    st.text_area("", placeholder="Write your response to Question 1 here...")
    st.write("""
    #### Question 2:
    Your firm follows and Internal Labor Market (ILM) strategy by hiring externally only for entry-level positions within each
    job and relying on internal promotions to fill higher-level roles, either within the same job or across jobs.
    1. What are the advantages and disadvantages of this approach for the firm and for its employees?
    2. To what extent does this approach support career development for employees?
    """)
    st.text_area("", placeholder="Write your response to Question 2 here...") 

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


