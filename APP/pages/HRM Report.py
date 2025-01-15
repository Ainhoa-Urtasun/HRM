import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

    
user_text = st.text_area("Your text here:", placeholder="Type something...")
    
# Set page configuration
st.set_page_config(page_title="HRM Report", layout="wide")

# Navigation menu
selected = option_menu(
    menu_title="",  # No title for the menu
    options=["HRM Report"],  # Menu options
    icons=["book"],  # Icons for options
    menu_icon="cast",  # Icon for the menu
    default_index=0,  # Default selected option
    orientation="vertical",
)

