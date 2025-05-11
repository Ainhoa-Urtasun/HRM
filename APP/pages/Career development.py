import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Career_development():
    st.title("Tournament Model")

    # Sidebar: Parameters
    w = st.sidebar.slider("Δw (Salary Increase)", min_value=1.0, max_value=50.0, value=20.0, step=1.0)
    g_1 = st.sidebar.slider("Skill Gap - Employee 1 (g₁)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
    g_2 = st.sidebar.slider("Skill Gap - Employee 2 (g₂)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)

    # Effort range (common for comparison)
    e_range = np.linspace(0.1, 20, 300)

    # Calculate common Marginal Revenue (MR), which is symmetric
    ratio = np.sqrt(g_1 / g_2)
    mr_common = w * ratio / (e_range * (1 + ratio) ** 2)

    # Calculate Marginal Costs (MC) for each employee
    mc_1 = 2 * g_1 * e_range
    mc_2 = 2 * g_2 * e_range

    # Optimal Efforts
    opt_e1 = w / (2 * g_1)
    opt_e2 = w / (2 * g_2)

    # Calculate Marginal Revenue at Optimal Efforts
    e2_equilibrium = np.sqrt(g_1 / g_2) * opt_e1
    mr_1_at_opt = w * e2_equilibrium / (opt_e1 + e2_equilibrium) ** 2

    e1_equilibrium = np.sqrt(g_2 / g_1) * opt_e2
    mr_2_at_opt = w * e1_equilibrium / (opt_e2 + e1_equilibrium) ** 2

    # Plotting
    plt.figure(figsize=(10, 6))

    # Marginal Revenue (same for both employees)
    plt.plot(e_range, mr_common, '--', color='black', label="Marginal Revenue (Same for Both)")

    # Marginal Costs
    plt.plot(e_range, mc_1, label="Marginal Cost - Employee 1 (g₁)")
    plt.plot(e_range, mc_2, label="Marginal Cost - Employee 2 (g₂)")

    # Plot Settings
    plt.xlabel("Effort Level (e)")
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 5)
    plt.ylim(0, 100)

    st.pyplot(plt)

    st.write("""
    #### Question 1: 
    At the end of 2023, your firm promoted 1 woman and 1 man from the job category 'Support Intellectuals and Scientists, Technicians, and 
    Professionals' to 'Other Managers'. Additionally, during 2023, 2 women and 3 men from this job left the firm. Assume
    there were no other workforce movements.
    1. Calculate the turnover rate for this job category by gender.
    2. Explain the formula you used for the calculation.
    """)
    st.text_area("", placeholder="Write your response to Question 1 here...")

# Streamlit App Setup
st.set_page_config(page_title="Career Development", layout="wide")

# Navigation
selected = option_menu(
    menu_title="",
    options=["Career development"],
    icons=["person"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical"
)

if selected == "Career development":
    Career_development()






   
