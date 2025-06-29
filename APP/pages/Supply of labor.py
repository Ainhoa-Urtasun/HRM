import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Supply of labor", layout="wide")

def isoquants():
    st.title("Isoquants: Supply of Labor")

    # Interactive wage
    w = st.sidebar.slider("w (Pay per hour of work)", min_value=0.1, max_value=1.0, value=0.5, step=0.1)

    H = np.linspace(1, 10, 200)

    # Plot
    fig, ax = plt.subplots(figsize=(9, 6))

    for U in [9, 10, 11]:
        ax.plot(H, U - np.log(H), label=f'Isoquant: U={U}')

    ax.plot(H, w * (24 - H), '--', label=f'Time restriction: w={w:.2f}')

    ax.set_xlabel('Hours of Leisure (H)')
    ax.set_ylabel('Income = wL')
    ax.legend()
    ax.grid(True)
    ax.set_xlim(0, 10)

    st.pyplot(fig)

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
