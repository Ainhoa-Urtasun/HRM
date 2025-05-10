import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Career_development():
    st.title("Tournament Model: Marginal Revenue and Marginal Cost")

    # Sidebar inputs for parameters
    w = st.sidebar.slider("Salary Increase (w)", min_value=1.0, max_value=70.0, step=1.0)
    g_1 = st.sidebar.slider("Skill Gap - Employee 1 (g1)", min_value=0.1, max_value=1.0, step=0.1)
    g_2 = st.sidebar.slider("Skill Gap - Employee 2 (g2)", min_value=0.1, max_value=1.0, step=0.1)

    # Effort range for plotting
    e_range = np.linspace(0.1, 20, 300)

    # Calculate Marginal Revenue and Marginal Cost for both employees
    mr_1 = w * np.sqrt(g_1/g_2) / e_range * (1 + np.sqrt(g_1/g_2))**2 
    mc_1 = 2 * g_1 * e_range

    mr_2 = w * np.sqrt(g_2/g_1) / e_range * (1 + np.sqrt(g_2/g_1))**2 
    mc_2 = 2 * g_2 * e_range

    # Create figure and two Y-axes
    fig, ax1 = plt.subplots(figsize=(8, 6))

    ax2 = ax1.twinx()

    # Plot Marginal Revenue on ax1 (left Y-axis)
    ax1.plot(e_range, mr_1, '--', label="MR - Employee 1", color='blue')
    ax1.plot(e_range, mr_2, '--', label="MR - Employee 2", color='cyan')
    ax1.set_ylabel("Marginal Revenue", color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Plot Marginal Cost on ax2 (right Y-axis)
    ax2.plot(e_range, mc_1, label="MC - Employee 1", color='red')
    ax2.plot(e_range, mc_2, label="MC - Employee 2", color='orange')
    ax2.set_ylabel("Marginal Cost", color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Titles and labels
    ax1.set_xlabel("Effort Level (e)")
    plt.title("Marginal Revenue and Marginal Cost for Both Employees")

    # Combine legends from both axes
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper right")

    st.pyplot(fig)

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

   
