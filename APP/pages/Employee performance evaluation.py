import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Page configuration must be at the top
st.set_page_config(page_title="Employee performance evaluation", layout="wide")

def Employee_performance():
    # Sidebar inputs for employee skills
    st.sidebar.write("Vector of skills possessed by the employee:")
    with st.sidebar.expander("Vector of Skills Possessed by the Employee"):
        s1 = st.number_input("Demonstrating willingness to learn", key='s1_emp', min_value=0, max_value=100, step=1)
        s2 = st.number_input("Collaborating in teams and networks", key='s2_emp', min_value=0, max_value=100, step=1)
        s3 = st.number_input("Working efficiently", key='s3_emp', min_value=0, max_value=100, step=1)
        s4 = st.number_input("Taking a proactive approach", key='s4_emp', min_value=0, max_value=100, step=1)

    # Sidebar inputs for required skills
    st.sidebar.write("Vector of required skills for the job:")
    with st.sidebar.expander("Vector of Required Skills"):
        s1k = st.number_input("Demonstrating willingness to learn", key='s1_req', min_value=0, max_value=100, step=1)
        s2k = st.number_input("Collaborating in teams and networks", key='s2_req', min_value=0, max_value=100, step=1)
        s3k = st.number_input("Working efficiently", key='s3_req', min_value=0, max_value=100, step=1)
        s4k = st.number_input("Taking a proactive approach", key='s4_req', min_value=0, max_value=100, step=1)

    # Calculate skill gap
    employee_skills = np.array([s1, s2, s3, s4]) / np.sqrt(5)
    required_skills = np.array([s1k, s2k, s3k, s4k]) / np.sqrt(5)
    gap = np.sqrt(np.sum((required_skills - employee_skills) ** 2))

    st.write(f"Skill Gap: {gap:.2f}")

    # Define effort levels and calculate cost of effort
    e = np.linspace(1, 10, 100)  # Example effort levels
    cost_of_effort = gap * e**2

    # Plot the cost of effort
    fig = plt.figure(figsize=(5, 5), dpi=100)
    plt.plot(e, cost_of_effort, color='red')
    plt.xlabel("Effort (e)")
    plt.title("Cost of Effort Function")
    plt.legend()
    st.pyplot(fig)

# Option menu
selected = option_menu(
    menu_title="",  # required
    options=['Employee performance evaluation'],  # required
    icons=['people'],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Employee performance evaluation":
    Employee_performance()
