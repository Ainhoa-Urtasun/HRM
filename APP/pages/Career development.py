import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Career_development():
    st.title("Tournament Model: Symmetric Marginal Revenue and Different Marginal Costs")

    # Sidebar: Parameters
    w = st.sidebar.slider("Salary Increase (w)", min_value=1.0, max_value=70.0, value=20.0, step=1.0)
    g_1 = st.sidebar.slider("Skill Gap - Employee 1 (g₁)", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    g_2 = st.sidebar.slider("Skill Gap - Employee 2 (g₂)", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

    # Effort range (common for comparison)
    e_range = np.linspace(0.1, 20, 300)

    # Calculate common Marginal Revenue (MR), which is symmetric
    ratio = np.sqrt(g_1 / g_2)
    mr_common = w * ratio / (e_range * (1 + ratio) ** 2)

    # Calculate Marginal Costs (MC) for each employee
    mc_1 = 2 * g_1 * e_range
    mc_2 = 2 * g_2 * e_range

    # Optimal Effort Levels
    opt_e1 = w / (2 * g_1)
    opt_e2 = w / (2 * g_2)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Marginal Revenue (same for both employees)
    plt.plot(e_range, mr_common, '--', color='black', label="Marginal Revenue (Same for Both)")

    # Marginal Costs for each employee
    plt.plot(e_range, mc_1, label="Marginal Cost - Employee 1 (g₁)")
    plt.plot(e_range, mc_2, label="Marginal Cost - Employee 2 (g₂)")

    # Mark Optimal Effort Levels
    plt.axvline(opt_e1, color='blue', linestyle=':', label=f"Optimal e₁ = {opt_e1:.2f}")
    plt.axvline(opt_e2, color='red', linestyle=':', label=f"Optimal e₂ = {opt_e2:.2f}")

    # Plot Settings
    plt.xlabel("Effort Level (e)")
    plt.ylabel("Value")
    plt.title("Symmetric Marginal Revenue and Different Marginal Costs")
    plt.legend()
    plt.grid(True)
    plt.ylim(0, 100)

    st.pyplot(plt)

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






   
