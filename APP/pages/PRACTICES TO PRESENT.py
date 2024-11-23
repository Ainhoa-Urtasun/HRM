import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT0_1():
  
  st.markdown("<h3 style='color: #4CAF50;'>🚀 Practices to present </h3>", unsafe_allow_html=True)
  st.write(
    '''
    In this course, students will complete **25 Practices**, each contributing 1% to their final grade. 
    These practices are divided into two types:

    - **Test & Quiz Practices**: exam-like questions for each unit 
    - **Interactive Practices**: selecting a firm and creating visuals through an app. Students will 
      also present their findings out loud, enhancing their communication skills.

    The table below summarizes the practices by unit and type:
    '''
  )
  
  st.markdown(
    '''
    | Unit    |  Test & Quiz Practices   | Interactive Practices         |
    |---------|--------------------------|-------------------------------|
    | Unit 1  | 1, 2                     | 3                             |
    | Unit 2  | 4, 5                     | 6                             |  
    | Unit 3  | 7, 8                     | 9                             |       
    | Unit 4  | 10, 11                   | 12 (present 3, 6, 9, 12)      |       


    **Resources**:
    - [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) from CEDEFOP (European Centre for the Development of Vocational Training)
    - [SABI](https://www.unavarra.es/biblioteca?languageId=1) from UPNA library
    '''
  )
  
st.set_page_config(page_title="PRACTICES TO PRESENT", layout="wide")
selected = option_menu(
  menu_title="",  # required
  options=['PRACTICES TO PRESENT'],  # required
  icons=['person'],  # optional
  menu_icon="cast",  # optional
  default_index=0,  # optional
  orientation="vertical",
)
if selected == 'PRACTICES TO PRESENT':
  UNIT0_1()
