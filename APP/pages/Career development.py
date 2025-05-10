import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Career_development():
    st.title("Tournament Model: Marginal Revenue and Marginal Cost")

    # Sidebar inputs for parameters
    w = st.sidebar.slider("Salary Increase (w)", min_value=1.0, max_value=200.0, step=1.0)
    g_1 = st.sidebar.slider("Skill Gap - Employee 1 (g1)", min_value=0.1, max_value=5.0, step=0.1)
    g_2 = st.sidebar.slider("Skill Gap - Employee 2 (g2)", min_value=0.1, max_value=5.0, step=0.1)

    # Constants for the error term ξ
    E_xi = 0.2
    Var_xi = 0.1

    # Effort range for plotting
    e_range = np.linspace(0.1, 20, 300)

    # Calculate Marginal Revenue and Marginal Cost for both employees
    mr_1 = w * np.sqrt(g_1/g_2) / e_range * (1 + np.sqrt(g_1/g_2))**2 
    mc_1 = 2 * g_1 * e_range

    mr_2 = w * np.sqrt(g_2/g_1) / e_range * (1 + np.sqrt(g_2/g_1))**2 
    mc_2 = 2 * g_2 * e_range

    # Plotting Marginal Revenue and Cost
    plt.figure(figsize=(8, 6))
    plt.plot(e_range, mr_1, label="Marginal Revenue - Employee 1", linestyle="--")
    plt.plot(e_range, mc_1, label="Marginal Cost - Employee 1")

    plt.plot(e_range, mr_2, label="Marginal Revenue - Employee 2", linestyle="--")
    plt.plot(e_range, mc_2, label="Marginal Cost - Employee 2")

    plt.xlabel("Effort Level (e)")
    plt.ylabel("Value")
    plt.title("Marginal Revenue and Marginal Cost for Both Employees")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Streamlit Page Configuration
st.set_page_config(page_title="Career Development", layout="wide")

# Menu Selection
selected = option_menu(
    menu_title="",
    options=["Career development"],
    icons=["person"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical"
)

# Call the selected section
if selected == "Career development":
    Career_development()



    
   
