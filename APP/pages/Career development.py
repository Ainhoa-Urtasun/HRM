import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Career_development():
    st.title("Tournament Model: Marginal Revenue and Marginal Cost")

    # Sidebar: Parameter Inputs
    w = st.sidebar.slider("Salary Increase (w)", min_value=1.0, max_value=70.0, value=20.0, step=1.0)
    g_1 = st.sidebar.slider("Skill Gap - Employee 1 (g₁)", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    g_2 = st.sidebar.slider("Skill Gap - Employee 2 (g₂)", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

    # Common effort range for both employees
    e_range = np.linspace(0.1, 20, 300)

    # Calculate Marginal Revenue (MR) for Employee 1
    ratio_1 = np.sqrt(g_1 / g_2)
    mr_1 = w * ratio_1 / (e_range * (1 + ratio_1) ** 2)
    mc_1 = 2 * g_1 * e_range

    # Calculate Marginal Revenue (MR) for Employee 2
    ratio_2 = np.sqrt(g_2 / g_1)
    mr_2 = w * ratio_2 / (e_range * (1 + ratio_2) ** 2)
    mc_2 = 2 * g_2 * e_range

    # Calculate Optimal Efforts (where MR = MC)
    opt_e1 = w / (2 * g_1)
    opt_e2 = w / (2 * g_2)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Employee 1 Curves
    plt.plot(e_range, mr_1, '--', label="MR - Employee 1 (Lower Skill Gap)")
    plt.plot(e_range, mc_1, label="MC - Employee 1 (Lower Skill Gap)")

    # Employee 2 Curves
    plt.plot(e_range, mr_2, '--', label="MR - Employee 2 (Higher Skill Gap)")
    plt.plot(e_range, mc_2, label="MC - Employee 2 (Higher Skill Gap)")

    # Mark Optimal Effort Levels
    plt.axvline(opt_e1, color='blue', linestyle=':', label=f"Optimal e₁ = {opt_e1:.2f}")
    plt.axvline(opt_e2, color='red', linestyle=':', label=f"Optimal e₂ = {opt_e2:.2f}")

    # Plot Annotations and Layout
    plt.xlabel("Effort Level")
    plt.ylabel("Value")
    plt.title("Marginal Revenue and Cost - Visualizing Optimal Effort Levels")
    plt.legend()
    plt.grid(True)
    plt.ylim(0, 100)  # Adjust Y-axis if needed

    st.pyplot(plt)

# Streamlit App Setup
st.set_page_config(page_title="Career Development", layout="wide")

# Navigation Menu
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




   
