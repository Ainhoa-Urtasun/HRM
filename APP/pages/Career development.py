import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Career_development():
    st.title("Tournament Model: Marginal Revenue and Marginal Cost")

    # Sidebar inputs for parameters
    w = st.sidebar.slider("Salary Increase (w)", min_value=10.0, max_value=200.0, value=70.0, step=1.0)
    g_1 = st.sidebar.slider("Skill Gap - Employee 1 (g1)", min_value=0.1, max_value=5.0, value=0.6, step=0.1)
    g_2 = st.sidebar.slider("Skill Gap - Employee 2 (g2)", min_value=0.1, max_value=5.0, value=1.2, step=0.1)
    R_1 = st.sidebar.slider("Risk Aversion - Employee 1 (R1)", min_value=0.0, max_value=0.01, value=0.0001, step=0.0001)
    R_2 = st.sidebar.slider("Risk Aversion - Employee 2 (R2)", min_value=0.0, max_value=0.01, value=0.0005, step=0.0001)

    # Constants for the error term ξ
    E_xi = 0.2
    Var_xi = 0.1

    # Effort range for plotting
    e_range = np.linspace(0.1, 20, 300)

    # Calculate Marginal Revenue and Marginal Cost for both employees
    mr_1 = w * (e_range * np.sqrt(g_1/g_2) / (e_range + e_range * np.sqrt(g_1/g_2))**2) 
    mc_1 = 2 * g_1 * e_range

    mr_2 = w * (e_range * np.sqrt(g_2/g_1) / (e_range + e_range * np.sqrt(g_2/g_1))**2)
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

    # Calculate Optimal Efforts based on MR = MC
    opt_e1 = round(w / (2 * g_1), 2)
    opt_e2 = round(w / (2 * g_2), 2)

    # Calculate Utilities
    def utility(w, e_i, e_j, E_xi, R, Var_xi, g):
        prob = e_i / (e_i + e_j) + E_xi
        return w * prob - R * w**2 * Var_xi - g * e_i**2

    U_1 = round(utility(w, opt_e1, opt_e2, E_xi, R_1, Var_xi, g_1), 2)
    U_2 = round(utility(w, opt_e2, opt_e1, E_xi, R_2, Var_xi, g_2), 2)

    # Display Results
    st.subheader("Calculated Optimal Efforts and Utilities")
    st.write(f"Employee 1 Optimal Effort: {opt_e1}, Utility: {U_1}")
    st.write(f"Employee 2 Optimal Effort: {opt_e2}, Utility: {U_2}")

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



    
   
