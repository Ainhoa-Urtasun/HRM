import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT0_1():
    st.markdown("<h3 style='color: #4CAF50;'>25 in-person activities, each contributing 1% to the final grade:</h3>", unsafe_allow_html=True)
    st.write(
        '''



        
        - **In-person activities 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23:** Exam-like questions
        - **In-person activities 3, 6, 8, 12, 18, 21, 24:** presentations
        - **In-person activities 15 to 25:** Power BI
        
        Students should do the presentations in pairs.

        The only requirement to participate in in-person activities is to be present in class. 
        No exceptions or justifications for absences will be accepted, regardless of the reason (illness, sports, family, etc.).

        **Online Resources**:
        - [MiAulario](https://miaulario.unavarra.es/portal) from UPNA
        - [HRM App](https://curvp4nsnitb9ukuuholt9.streamlit.app/)
        - [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) from CEDEFOP (European Centre for the Development of Vocational Training)
        - [SABI](https://www.unavarra.es/biblioteca?languageId=1) from UPNA library
        - [Power BI](https://vdibroker.unavarra.es/uds/page/login)
        '''
    )

st.set_page_config(page_title="Practices (25%)", layout="wide")

# Directly call the function since there's only one menu option for now.
UNIT0_1()
