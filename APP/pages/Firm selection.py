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
    Power BI, a highly demanded software developed by Microsoft, enables businesses to make data-driven decisions by seamlessly integrating and visualizing data. 
    Your firm has decided to implement this powerful tool. Describe how Power BI can support your firm in the performance of its economic activities activities
    """)
    st.text_area("", placeholder="Write your response to Question 1 here...")
    st.write("""
    #### Question 2:
    Which job within your firm should master the new technology? Why?
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


