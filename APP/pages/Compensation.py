import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def Compensation():
    
    # Sidebar for selecting a job
    st.sidebar.radio(
        "Select a job at your firm:",
        ("Other managers", "Support intellectuals and scientists, technicians and professionals", "Administrative employees")
    )
    
    # Sidebar expander for skill gap inputs
    with st.sidebar.expander("Skill gaps"):
        g1 = st.number_input(
            "Enter value for skill gap 1 (g₁):",
            key='g1',
            step=1,
            min_value=1,
            max_value=100,
            value=10
        )
        g2 = st.number_input(
            "Enter value for skill gap 2 (g₂):",
            key='g2',
            step=1,
            min_value=1,
            max_value=100,
            value=20
        )
    
    # Generate the plot
    w = np.linspace(0.1, 10, 100)
    fig = plt.figure(figsize=(5, 5), dpi=100)
    
    # Plot lines for both g1 and g2
    plt.plot(w, 2 * w / g1, label=f'g₁ = {g1}', color='blue')
    plt.plot(w, 2 * w / g2, label=f'g₂ = {g2}', color='orange')
    
    plt.title('Effort Supply Curve')
    plt.xlabel('Incentive rate')
    plt.ylabel('Effort')
    plt.legend()
    
    # Display the plot
    st.pyplot(fig)

    st.write("""
    #### Question 5: Who is more likely to increase effort in response to incentives? Why?:""")
    st.text_area("", placeholder="Write your response to Question 5 here...")

    st.write("""
    #### Question 6: Which type of motivation—intrinsic or extrinsic—does pay-for-performance trigger?:""")
    st.text_area("", placeholder="Write your response to Question 6 here...")

st.set_page_config(page_title="Compensation", layout="wide")

selected = option_menu(
    menu_title="",
    options=['Compensation'],
    icons=["book", "book", "people"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical",
)

if selected == "Compensation":
    Compensation()

