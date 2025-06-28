import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Isoquants():
    st.title("Isoquants")

    # Sidebar: Parameters
    w = st.sidebar.slider("w (Pay per hour of work)", min_value=0.0, max_value=1.0, value=0.1, step=0.1)

    # Days off
    H = np.linspace(1, 10, 200)

    # Plot setup
    plt.figure(figsize=(9, 6))

    # Isoquants
    plt.plot(H, 9 - np.log(H), label=f'Isoquant: U=9')
    plt.plot(H, 10 - np.log(H), label=f'Isoquant: U=10')
    plt.plot(H, 11 - np.log(H), label=f'Isoquant: U=11')
            
    # Time restriction:
    plt.plot(H, w * (24 - H), label=f'Time restriction')

    # Final touches
    plt.xlabel('Hours off (H)')
    plt.ylabel('Income (wL)')
    plt.grid(True)
    plt.legend()
    plt.xlim(0, 10)

    st.pyplot(plt)

# Streamlit App Setup
st.set_page_config(page_title="Isoquants", layout="wide")

# Navigation
selected = option_menu(
    menu_title="",
    options=["Isoquants"],
    icons=["person"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical"
)

if selected == "Isoquants":
    Isoquants()
