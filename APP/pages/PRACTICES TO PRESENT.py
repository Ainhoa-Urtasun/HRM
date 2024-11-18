import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT0_1():
  
  st.markdown("<h3 style='color: #4CAF50;'>🚀 Practices to present </h3>", unsafe_allow_html=True)

  st.write(
    '''
    - [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) from CEDEFOP (European Centre for the 
    Development of Vocational Training)
    - [SABI](https://www.unavarra.es/biblioteca?languageId=1) from the library at UPNA
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
