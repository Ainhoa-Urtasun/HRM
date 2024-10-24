import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():

    st.latex(r'''
    \text{CAGR} = \left( \frac{E_{n}}{E_{0}} \right)^{\frac{1}{n}} - 1
    ''')


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
    ax.set_title("Employment Over Time")
    ax.legend()
    st.pyplot(fig)

def UNIT4_2():
    st.write(
        '''
        In recruiting, **asymmetric information** arises when candidates know more about their abilities than the firm. 
    This can lead to **adverse selection**, where the firm might hire less qualified candidates because it lacks full information. 
    To mitigate this, candidates use **signaling** (e.g., qualifications, experience) to indicate their abilities, while firms engage 
    in **screening** (e.g., interviews, tests) to gather more information. Additionally, firms often use **probation periods** to assess 
    an employee’s true performance before making long-term commitments, reducing the risks of hiring based on incomplete information.
        '''
    )


st.set_page_config(page_title="UNIT4", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Employment","Asymmetric Information"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Employment":
    UNIT4_1()
if selected == "Asymmetric Information":
    UNIT4_2()

