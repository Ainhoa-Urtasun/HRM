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

    # Effort range for Employee 1
    e1_range = np.linspace(0.1, 20, 300)

    # Calculate Marginal Revenue (MR) and Marginal Cost (MC) for Employee 1
    ratio = np.sqrt(g_1 / g_2)
    e2_equilibrium = ratio * e1_range
    mr_1 = w * e2_equilibrium / (e1_range + e2_equilibrium) ** 2
    mc_1 = 2 * g_1 * e1_range

    # Optimal Effort for Employee 1
    opt_e1 = w / (2 * g_1)

    # Plotting
    plt.figure(figsize=(10, 6))

    # MR and MC curves
    plt.plot(e1_range, mr_1, '--', label="Marginal Revenue (MR)")
    plt.plot(e1_range, mc_1, label="Marginal Cost (MC)")

    # Mark Optimal Effort Level
    plt.axvline(opt_e1, color='blue', linestyle=':', label=f"Optimal Effort e₁ = {opt_e1:.2f}")

    # Layout
    plt.xlabel("Effort Level (e₁)")
    plt.ylabel("Value")
    plt.title("Marginal Revenue and Cost for Employee 1")
    plt.legend()
    plt.grid(True)
    plt.ylim(0, 100)  # Adjust for better visibility

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






   
