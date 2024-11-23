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

    - *Test and Quiz Practices*: exam-like questions for each unit 
    - *Interactive Practices*: selecting a firm and creating visuals through an app. Students will 
      also present their findings out loud, enhancing their communication skills.

    The table below summarizes the practices by type and unit:
    '''
)

st.markdown(
    '''
    | Type                  | Unit      | Practices | Notes                                                                 |
    |-----------------------|-----------|-----------|----------------------------------------------------------------------|
    | Test and Quiz         | Unit 1    | 1, 2      | Exam-like questions                                                  |
    |                       | Unit 2    | 4, 5      |                                                                      |
    |                       | Unit 3    | 6, 7      |                                                                      |
    |                       | Unit 4    | 9, 10     |                                                                      |
    | Interactive Practices | Unit 3    | 6, 7      | Selecting a firm and creating visuals through an app                 |
    |                       | Unit 6    | 12        |                                                                      |
    |                       | Unit 8    | 19        |                                                                      |
    |                       | Unit 12   | 25        | Presenting findings and communication skill enhancement              |

    **Resources**:
    - [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) from CEDEFOP (European Centre for the Development of Vocational Training)
    - [SABI](https://www.unavarra.es/biblioteca?languageId=1) from UPNA library
    '''
)


# Set page configuration
st.set_page_config(page_title="PRACTICES TO PRESENT", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['PRACTICES TO PRESENT'],  # required
    icons=['person'],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == 'PRACTICES TO PRESENT':
    UNIT0_1()
