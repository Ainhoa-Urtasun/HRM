import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def firm_selection():
  st.text_area("About your firm:", placeholder="Type its name, NACE Rev. Primary Code, and English trade description...")

st.set_page_config(page_title="Firm selection", layout="wide")
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




