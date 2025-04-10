import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Page configuration
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
        ax.set_xticks(years)
        ax.set_title("RULC Over Time")
        ax.set_xlabel("Year")
        ax.set_ylabel("RULC")
        ax.grid(True)
        st.pyplot(fig)

        st.write("""
        #### Question 1: Explain what you observe in the RULC trend:""")
        st.text_area("", placeholder = "Write your response to Question 1 here...")

        st.write("""
        #### Question 2: Classify RULC both as an output- or input-based KPI, and as a KPI reflecting the intensive or extensive margin:""")
        st.text_area("", placeholder = "Write your response to Question 2 here...")

    st.title("Production Function: $Q = L_{1}^{0.15} L_{2}^{0.25} L_{3}^{0.05} K^{0.2}$")
    A = st.number_input(
        "Enter the value for $L_{1}^{0.15} L_{3}^{0.05} K^{0.2}$ using 2023 SABI data, by adding up women and men in $L_1$, and in $L_3$, and assuming, for $K$ that each technology depreciates by €500,000 yearly):",
        min_value=0.1, step=0.1, format="%.2f")

    if A:
        L = np.linspace(1, 100, 100)
        Q = A * L**0.2

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(L, Q, color='green')
        ax.set_title("Production Function")
        ax.set_xlabel("$L_2$ (Support intellectuals and scientists, technicians and professionals)")
        ax.set_ylabel("$Q$ (Output)")
        ax.grid(True)
        st.pyplot(fig)

        st.write("""
        #### Question 3: Evaluate the output elasticity of $L_{2}$ at different points of the production function:""")
        st.text_area("", placeholder = "Write your response to Question 3 here...")

        st.write("""
        #### Question 4: Classify the output elasticity of $L_2$ both as an output- or input-based KPI, and as a KPI reflecting the intensive or extensive margin::""")
        st.text_area("", placeholder = "Write your response to Question 4 here...")

# Option menu
selected = option_menu(
    menu_title="",
    options=['Employee performance evaluation'],
    icons=['people'],
    menu_icon="cast",
    default_index=0,
    orientation="vertical",
)

if selected == "Employee performance evaluation":
    Employee_performance()


