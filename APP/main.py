import streamlit as st
from streamlit_option_menu import option_menu
from UNIT1 import UNIT1
from UNIT2 import UNIT2

st.set_page_config(layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["UNIT 1. HRM", "UNIT 2. JOB ANALYSIS AND DESIGN"],  # required
    icons=["book", "archive"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

if selected == "UNIT 1. HRM":
    UNIT1()  # Call the function defined in UNIT1.py
elif selected == "UNIT 2. JOB ANALYSIS AND DESIGN":
    UNIT2()  # Call the function defined in UNIT2.py

