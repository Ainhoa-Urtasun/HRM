import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT2_1():
    st.title("O*NET")
    st.markdown(
        "[O*NET Online](https://www.onetonline.org/) is a comprehensive tool for career exploration and job analysis. "
        "It offers detailed descriptions of the tasks, skills, and other attributes required for more than 1,000 jobs, "
        "making it an invaluable resource for job seekers, workforce development professionals, and HR specialists. "
        "By providing standardized information on various job roles, O*NET Online facilitates job analysis and design, "
        "helping users understand the specific demands and characteristics of different occupations."
    )

def UNIT2_2():
    st.title("Work Activities (A)")
    st.write(
        "A **work activity** (A) is an action performed by an individual that results in a specific output. "
        "Jobs are collections of work activities. Every firm transforms inputs into outputs (goods and services). "
        "The nature of these outputs determines both the industry classification of the firm and the work activities its employees must perform. "
        "This highlights the importance of understanding industry classifications. O*NET identifies 41 distinct work activities, "
        "but for simplicity, we focus on 4 working activities (A):"
    )

st.set_page_config(page_title="UNIT1", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Industries and Occupations", "Notation for the Course", "Earnings Before Interests and Taxes (EBIT)", "Cost of Employees", "EBIT Optimization"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Industries and Occupations":
    UNIT1_1()
elif selected == "Notation for the Course":
    UNIT1_2()
elif selected == "Earnings Before Interests and Taxes (EBIT)":
    UNIT1_3()
elif selected == "Cost of Employees":
    UNIT1_4()
elif selected == "EBIT Optimization":
    UNIT1_5()

