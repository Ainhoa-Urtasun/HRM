import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Function for job analysis and design
def job_analysis_and_design():
    st.sidebar.radio(
        "Select a job at your firm:",
        ("Other managers", "Support intellectuals and scientists", "Technicians and professionals", "Sales representatives and similar")
    )
    st.sidebar.write("Evaluate the job:")

    # Input sections for different skill categories
    with st.sidebar.expander("Intellectual"):
        s11 = st.number_input("Willingness to learn", key='s11', min_value=0, max_value=100, value=50, step=1)
        s12 = st.number_input("Team collaboration", key='s12', min_value=0, max_value=100, value=50, step=1)
        s13 = st.number_input("Efficiency", key='s13', min_value=0, max_value=100, value=50, step=1)
        s14 = st.number_input("Proactivity", key='s14', min_value=0, max_value=100, value=50, step=1)
        
    with st.sidebar.expander("Physical"):
        s21 = st.number_input("Physical stamina", key='s21', min_value=0, max_value=100, value=50, step=1)
        s22 = st.number_input("Dexterity", key='s22', min_value=0, max_value=100, value=50, step=1)
        s23 = st.number_input("Endurance", key='s23', min_value=0, max_value=100, value=50, step=1)
        s24 = st.number_input("Strength", key='s24', min_value=0, max_value=100, value=50, step=1)
        
    with st.sidebar.expander("Social"):
        s31 = st.number_input("Communication skills", key='s31', min_value=0, max_value=100, value=50, step=1)
        s32 = st.number_input("Conflict resolution", key='s32', min_value=0, max_value=100, value=50, step=1)
        s33 = st.number_input("Empathy", key='s33', min_value=0, max_value=100, value=50, step=1)
        s34 = st.number_input("Team leadership", key='s34', min_value=0, max_value=100, value=50, step=1)
        
    with st.sidebar.expander("Use of Methods"):
        s41 = st.number_input("Problem-solving", key='s41', min_value=0, max_value=100, value=50, step=1)
        s42 = st.number_input("Critical thinking", key='s42', min_value=0, max_value=100, value=50, step=1)
        s43 = st.number_input("Innovation", key='s43', min_value=0, max_value=100, value=50, step=1)
        s44 = st.number_input("Decision-making", key='s44', min_value=0, max_value=100, value=50, step=1)
        
    with st.sidebar.expander("Use of Technology"):
        s51 = st.number_input("IT skills", key='s51', min_value=0, max_value=100, value=50, step=1)
        s52 = st.number_input("Technical expertise", key='s52', min_value=0, max_value=100, value=50, step=1)
        s53 = st.number_input("Adaptability to tools", key='s53', min_value=0, max_value=100, value=50, step=1)
        s54 = st.number_input("System management", key='s54', min_value=0, max_value=100, value=50, step=1)

    # Create matrix and calculate norms
    matrix = np.array([
        [s11, s12, s13, s14],
        [s21, s22, s23, s24],
        [s31, s32, s33, s34],
        [s41, s42, s43, s44],
        [s51, s52, s53, s54],
    ])
    st.write("Skill Matrix:", matrix)
    norms = np.linalg.norm(matrix, axis=0)
    st.write("Norms for each skill dimension:", norms)

    # Input for job evaluation
    st.text_area("Describe the connection between your firm and the evaluated job:", placeholder="Explain here...")

# Streamlit page setup
st.set_page_config(page_title="Job Analysis and Design", layout="wide")

# Option menu
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





