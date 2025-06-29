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
    
    H = np.linspace(1, 10, 200)
    
    # Plot setup
    plt.figure(figsize=(9, 6))
    
    # Isoquants
    plt.plot(H, 9 - np.log(H), label=f'Isoquant: U=9')
    plt.plot(H, 10 - np.log(H), label=f'Isoquant: U=10')
    plt.plot(H, 11 - np.log(H), label=f'Isoquant: U=11')

    # Time restriction:
    w = 0.4
    plt.plot(H, w * (24 - H), label=f'Time restriction w = 0.4')

    # Final touches
    plt.xlabel('Hours off (H)')
    plt.ylabel('Income (wL)')
    plt.grid(True)
    plt.legend()
    plt.xlim(0, 10)
    st.pyplot(fig)

# Navigation
selected = option_menu(
    menu_title="",
    options=["Supply of labor"],
    icons=["graph-up"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical"
)

if selected == "Supply of labor":
    isoquants()
