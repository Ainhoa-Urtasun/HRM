import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Career_development():
    st.title("Tournament Model")

    # Sidebar: Parameters
    w = st.sidebar.slider("Δw (Salary Increase)", min_value=1.0, max_value=20.0, value=20.0, step=1.0)
    g_1 = st.sidebar.slider("Skill Gap - Employee 1 (g₁)", min_value=0.01, max_value=5.0, step=0.01)
    g_2 = st.sidebar.slider("Skill Gap - Employee 2 (g₂)", min_value=0.01, max_value=5.0, step=0.01)

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
    plt.ylim(0, 25)

    st.pyplot(plt)

    st.write("""
    #### Question 3: 
    Calculate the value of the marginal revenue and of the marginal cost for each employee as a function of their
    respective level of effort.
    """)
    st.text_area("", placeholder="Write your response to Question 3 here...")

    st.write("""
    #### Question 4: 
    Who exerts more effort to compete for the promotion? Explain why, referring to the relationship between skill gaps, marginal costs, and incentives.
    """)
    st.text_area("", placeholder="Write your response to Question 4 here...")

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






   
