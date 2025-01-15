import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def job_analysis_and_design():
    st.sidebar.radio(
        "Select a job at your firm:",
        ("other managers", "support intellectuals and scientists, technicians and professionals", "sales representatives and similar")
    )
    st.sidebar.write("Evaluate the job:")
    
    # Input sections for different skill categories
    with st.sidebar.expander("Intellectual"):
        s11 = st.number_input("Demonstrating willingness to learn", key='s11', min_value=0, max_value=100, step=1)
        s12 = st.number_input("Collaborating in teams and networks", key='s12', min_value=0, max_value=100, step=1)
        s13 = st.number_input("Working efficiently", key='s13', min_value=0, max_value=100, step=1)
        s14 = st.number_input("Taking a proactive approach", key='s14', min_value=0, max_value=100, step=1)
        
    with st.sidebar.expander("Physical"):
        s21 = st.number_input("Demonstrating willingness to learn", key='s21', min_value=0, max_value=100, step=1)
        s22 = st.number_input("Collaborating in teams and networks", key='s22', min_value=0, max_value=100, step=1)
        s23 = st.number_input("Working efficiently", key='s23', min_value=0, max_value=100, step=1)
        s24 = st.number_input("Taking a proactive approach", key='s24', min_value=0, max_value=100, step=1)
        
    with st.sidebar.expander("Social"):
        s31 = st.number_input("Demonstrating willingness to learn", key='s31', min_value=0, max_value=100, step=1)
        s32 = st.number_input("Collaborating in teams and networks", key='s32', min_value=0, max_value=100, step=1)
        s33 = st.number_input("Working efficiently", key='s33', min_value=0, max_value=100, step=1)
        s34 = st.number_input("Taking a proactive approach", key='s34', min_value=0, max_value=100, step=1)
        
    with st.sidebar.expander("Use of Methods"):
        s41 = st.number_input("Demonstrating willingness to learn", key='s41', min_value=0, max_value=100, step=1)
        s42 = st.number_input("Collaborating in teams and networks", key='s42', min_value=0, max_value=100, step=1)
        s43 = st.number_input("Working efficiently", key='s43', min_value=0, max_value=100, step=1)
        s44 = st.number_input("Taking a proactive approach", key='s44', min_value=0, max_value=100, step=1)
        
    with st.sidebar.expander("Use of Technology"):
        s51 = st.number_input("Demonstrating willingness to learn", key='s51', min_value=0, max_value=100, step=1)
        s52 = st.number_input("Collaborating in teams and networks", key='s52', min_value=0, max_value=100, step=1)
        s53 = st.number_input("Working efficiently", key='s53', min_value=0, max_value=100, step=1)
        s54 = st.number_input("Taking a proactive approach", key='s54', min_value=0, max_value=100, step=1)

    # Constructing the skill matrix
    matrix = np.array([
        [s11, s12, s13, s14],
        [s21, s22, s23, s24],
        [s31, s32, s33, s34],
        [s41, s42, s43, s44],
        [s51, s52, s53, s54],
    ])
    
    st.write(matrix)
    norms = (5**(-0.5)) * np.linalg.norm(matrix, axis=0)
    st.write(norms)

st.set_page_config(page_title="Job analysis and design", layout="wide")
selected = option_menu(
    menu_title="",  # No title for the menu
    options=["Job analysis and design"],  # Menu options
    icons=["book"],  # Icons for options
    menu_icon="cast",  # Icon for the menu
    default_index=0,  # Default selected option
    orientation="vertical",
)
# Call the selected section
if selected == "Job analysis and design":
    job_analysis_and_design()




