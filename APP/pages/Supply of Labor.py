import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Streamlit Setup
st.set_page_config(page_title="Supply of labor", layout="wide")

def isoquants():
    st.title("Isoquants")

    # Sidebar: Parameters
    w = st.sidebar.slider("w (Pay per hour of work)", min_value=0.1, max_value=1.0, value=0.5, step=0.1)

    # Hours off (leisure time)
    H = np.linspace(1, 10, 200)
    L = 24 - H  # Working hours

    # Initialize figure
    fig, ax = plt.subplots(figsize=(9, 6))

    # Isoquants: U = Income + ln(H) → Income = U - ln(H)
    for U in [9, 10, 11]:
        ax.plot(H, U - np.log(H), label=f'Isoquant: U={U}')

    # Time restriction line: Income = w * L = w * (24 - H)
    ax.plot(H, w * L, label=f'Time constraint: w={w}', linestyle='--')

    # Labels and legends
    ax.set_xlabel('Hours of Leisure (H)')
    ax.set_ylabel('Income = wL')
    ax.legend()
    ax.grid(True)
    ax.set_xlim(0, 10)

    st.pyplot(fig)

# Navigation
selected = option_menu(
    menu_title="",
    options=["Isoquants"],
    icons=["graph-up"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical"
)

if selected == "Supply of labor":
    isoquants()
