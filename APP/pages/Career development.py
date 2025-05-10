import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Career_development():
    st.title("Tournament Model: Marginal Revenue and Marginal Cost")

    # Sidebar: Parameters
    w = st.sidebar.slider("Salary Increase (w)", min_value=1.0, max_value=70.0, value=20.0, step=1.0)
    g_1 = st.sidebar.slider("Skill Gap - Employee 1 (g₁)", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    g_2 = st.sidebar.slider("Skill Gap - Employee 2 (g₂)", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

    # Effort ranges for each employee
    e1_range = np.linspace(0.1, 20, 300)
    e2_range = np.linspace(0.1, 20, 300)

    # Employee 1 MR and MC (function of e1)
    ratio_1 = np.sqrt(g_1 / g_2)
    e2_equilibrium = ratio_1 * e1_range
    mr_1 = w * e2_equilibrium / (e1_range + e2_equilibrium) ** 2
    mc_1 = 2 * g_1 * e1_range

    # Employee 2 MR and MC (function of e2)
    ratio_2 = np.sqrt(g_2 / g_1)
    e1_equilibrium = ratio_2 * e2_range
    mr_2 = w * e1_equilibrium / (e2_range + e1_equilibrium) ** 2
    mc_2 = 2 * g_2 * e2_range

    # Optimal Effort Levels
    opt_e1 = w / (2 * g_1)
    opt_e2 = w / (2 * g_2)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Employee 1
    plt.plot(e1_range, mr_1, '--', label="MR - Employee 1 (Own Effort e₁)")
    plt.plot(e1_range, mc_1, label="MC - Employee 1 (Own Effort e₁)")

    # Employee 2
    plt.plot(e2_range, mr_2, '--', label="MR - Employee 2 (Own Effort e₂)")
    plt.plot(e2_range, mc_2, label="MC - Employee 2 (Own Effort e₂)")

    # Mark Optimal Effort Levels
    plt.axvline(opt_e1, color='blue', linestyle=':', label=f"Optimal e₁ = {opt_e1:.2f}")
    plt.axvline(opt_e2, color='red', linestyle=':', label=f"Optimal e₂ = {opt_e2:.2f}")

    # Layout
    plt.xlabel("Effort Level (e₁ or e₂)")
    plt.ylabel("Value")
    plt.title("Marginal Revenue and Cost: Showing Optimal Effort Choices")
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





   
