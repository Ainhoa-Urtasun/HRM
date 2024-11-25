import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT0_1():
    st.markdown("<h3 style='color: #4CAF50;'>Consisting of 25 in-class activities, each contributing 1% to the final grade. Types:</h3>", unsafe_allow_html=True)
    st.write(
        '''
        - **In-class activities 1 to 8 and 13 to 19**: Exam-like questions for each unit
        - **In-class activities 9 to 12**: Mid-semester presentations
        - **In-class activities 20 to 24**: End-of-semester presentations
        - **In-class activity 25** to evaluate the cohesiveness and connection between the presentations
        
        Students can do the presentations individually or in pairs

        **Online Resources**:
        - [MiAulario](https://miaulario.unavarra.es/portal/site/2024_0_174404_81/page/9b199711-4fb6-46e7-b7de-a3e202b264f8)
        - [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) from CEDEFOP (European Centre for the Development of Vocational Training)
        - [SABI](https://www.unavarra.es/biblioteca?languageId=1) from UPNA library
        '''
    )

st.set_page_config(page_title="Practices (25%)", layout="wide")

# Directly call the function since there's only one menu option for now.
UNIT0_1()
