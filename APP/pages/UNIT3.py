import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT3_1():
    st.write("**Employment**: The total number of people currently working for the firm, including both full-time and part-time employees.")
    st.write("**New Hires**: The number of individuals who have recently been recruited and started working at the firm.")
    st.write("**Job Postings**: Advertisements made by the firm to fill open positions, specifying required qualifications and job responsibilities.")
    st.write("**Job Vacancies (or Job Openings)**: The number of available positions at the firm that are not yet filled and for which the firm is actively seeking candidates.")
    st.write("**Separations**: The total number of employees who leave the firm, either voluntarily (quitting, retiring) or involuntarily (layoffs, dismissals).")
    
    st.write(
        '''
        In recruiting, **asymmetric information** arises when candidates know more about their abilities than the firm. 
    This can lead to **adverse selection**, where the firm might hire less qualified candidates because it lacks full information. 
    To mitigate this, candidates use **signaling** (e.g., qualifications, experience) to indicate their abilities, while firms engage 
    in **screening** (e.g., interviews, tests) to gather more information. Additionally, firms often use **probation periods** to assess 
    an employee’s true performance before making long-term commitments, reducing the risks of hiring based on incomplete information.
        '''
    )

def UNIT3_2():
    st.write(
        '''. Next, we practice how to use them
        to calculate labor productivity and ULC.
        '''
    )
    st.components.v1.iframe("https://www.unavarra.es/biblioteca?languageId=1", width=800, height=600, scrolling=True)
    
    employees_input = st.sidebar.text_input("Number of Employees (comma-separated for 2019, 2020, 2021):", "1,1,1")
    employees = np.fromstring(employees_input, sep=',')
        
    df = pd.DataFrame({
        "Year": ["2019", "2020", "2021"],
        "Employment": employees,
    })

    fig, ax = plt.subplots()
    ax.plot(["2019", "2020", "2021"], employees, marker='x', label='Employment')    
    ax.set_xlabel('Year')
    ax.set_ylabel('Metrics')
    ax.set_title("Trends in employment")
    ax.legend()
    st.pyplot(fig)



st.set_page_config(page_title="UNIT3", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Terminology","Employment"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Terminology":
    UNIT3_1()
if selected == "Employment":
    UNIT3_2()

