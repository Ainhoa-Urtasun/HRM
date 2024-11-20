import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT8_1():
    
    # Sidebar input for e1
    e1 = st.sidebar.slider("Employee 1 decides how much effort to exert", min_value=1.0, max_value=100.0, step=0.1)

    # Generate e2 based on the formula
    e2 = lambda e1: (100 / e1**0.5)**(10/3)

    # Create a range of e1 values for visualization
    e1_values = np.linspace(1, 100, 500)
    e2_values = e2(e1_values)

    # Plot the curve
    plt.figure(figsize=(8, 6))
    plt.plot(e1_values, e2_values, label="Isoquant for Q = 100, \alpha_1 = 0.5, \alpha_2 = 0.3")
    plt.scatter(e1, e2(e1), color='red', label=f"Selected e1: {e1}, e2: {e2(e1):.2f}")
    plt.title("Visualization of e2 as a function of e1")
    plt.xlabel("Level of effort exerted by employee 1")
    plt.ylabel("Level of effort exerted by employee 2")
    plt.legend()
    plt.grid()

    # Display the plot in Streamlit
    st.pyplot(plt)

st.set_page_config(page_title="UNIT 8. CAREER DEVELOPMENT Career", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['UNIT 8. CAREER DEVELOPMENT'],  # required
    icons=["person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "UNIT 8. CAREER DEVELOPMENT":
    UNIT8_1()


    
   
