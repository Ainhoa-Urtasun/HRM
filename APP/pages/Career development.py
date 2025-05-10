import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Career_development():
    st.title("Tournament Model: Marginal Revenue and Marginal Cost")

    # Sidebar inputs for model parameters
    w = st.sidebar.slider("Salary Increase (w)", min_value=1.0, max_value=70.0, value=20.0, step=1.0)
    g_1 = st.sidebar.slider("Skill Gap - Employee 1 (g₁)", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    g_2 = st.sidebar.slider("Skill Gap - Employee 2 (g₂)", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

    # Effort ranges
    e1_range = np.linspace(0.1, 20, 300)
    e2_range = np.linspace(0.1, 20, 300)

    # Calculate efforts in equilibrium
    e2_equilibrium = np.sqrt(g_1 / g_2) * e1_range
    e1_equilibrium = np.sqrt(g_2 / g_1) * e2_range

    # Marginal Revenue calculations
    mr_1 = w * e2_equilibrium / (e1_range + e2_equilibrium) ** 2
    mc_1 = 2 * g_1 * e1_range

    mr_2 = w * e1_equilibrium / (e2_range + e1_equilibrium) ** 2
    mc_2 = 2 * g_2 * e2_range

    # Optimal effort levels
    opt_e1 = w / (2 * g_1)
    opt_e2 = w / (2 * g_2)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Employee 1 curves
    plt.plot(e1_range, mr_1, '--', label="MR - Employee 1")
    plt.plot(e1_range, mc_1, label="MC - Employee 1")

    # Employee 2 curves
    plt.plot(e2_range, mr_2, '--', label="MR - Employee 2")
    plt.plot(e2_range, mc_2, label="MC - Employee 2")

    # Optimal Effort Markers
    plt.axvline(opt_e1, color='blue', linestyle=':', label=f"Optimal e₁ = {opt_e1:.2f}")
    plt.axvline(opt_e2, color='red', linestyle=':', label=f"Optimal e₂ = {opt_e2:.2f}")

    # Labels and Layout
    plt.xlabel("Effort Level")
    plt.ylabel("Value")
    plt.title("Marginal Revenue and Marginal Cost for Both Employees")
    plt.legend()
    plt.grid(True)
    plt.ylim(0, 100)  # Adjust Y-axis limit if needed for visibility

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



   
