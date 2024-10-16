import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT2_1():
    st.write("**Employment**: The total number of people currently working for the firm, including both full-time and part-time employees.")
    st.write("**New Hires**: The number of individuals who have recently been recruited and started working at the firm.")
    st.write("**Job Postings**: Advertisements made by the firm to fill open positions, specifying required qualifications and job responsibilities.")
    st.write("**Separations**: The total number of employees who leave the firm, either voluntarily (quitting, retiring) or involuntarily (layoffs, dismissals).")

st.set_page_config(page_title="UNIT3", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Terminology"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Terminology":
    UNIT3_1()

