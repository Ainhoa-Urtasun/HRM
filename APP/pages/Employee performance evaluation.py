import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Page configuration must be at the top
st.set_page_config(page_title="Employee performance evaluation", layout="wide")

def Employee_performance():

    st.title("Real Unit Labor Cost (RULC) Visualization")
    st.write("Please enter your firm's RULC for the following years:")

    r2021 = st.number_input("RULC for 2021", min_value=0.0, step=0.01, format="%.2f")
    r2022 = st.number_input("RULC for 2022", min_value=0.0, step=0.01, format="%.2f")
    r2023 = st.number_input("RULC for 2023", min_value=0.0, step=0.01, format="%.2f")

    if all(v is not None for v in [r2021, r2022, r2023]):
        years = [2021, 2022, 2023]
        values = [r2021, r2022, r2023]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(years, values, marker='o', linestyle='-', color='blue')
        ax.set_title("RULC Over Time")
        ax.set_xlabel("Year")
        ax.set_ylabel("RULC")
        ax.grid(True)
        st.pyplot(fig)

    st.title("Production Function: $Q = L_{1}^{0.15} L_{2}^{0.25} L_{3}^{0.05} K^{0.2}$")
    A = st.number_input(
        "Enter here the value for $L_{1}^{0.15} L_{3}^{0.05} K^{0.2}$ using 2023 SABI data for $L_1$, $L_3$, and $K$ (assume each technology depreciates €1M yearly):",
        min_value=0.1, step=0.1, format="%.2f")

    if A:
        L = np.linspace(1, 100, 100)
        Q = A * L**0.2

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(L, Q, color='green')
        ax.set_title("Production Function: Q = A · L⁰·²")
        ax.set_xlabel("Labor (L)")
        ax.set_ylabel("Output (Q)")
        ax.grid(True)
        st.pyplot(fig)

# Option menu
selected = option_menu(
    menu_title="",  # required
    options=['Employee performance evaluation'],  # required
    icons=['people'],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Employee performance evaluation":
    Employee_performance()
