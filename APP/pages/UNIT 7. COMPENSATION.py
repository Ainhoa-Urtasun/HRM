import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def UNIT7_1():
 
    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 22 </h3>", unsafe_allow_html=True)
    
    # Sidebar for selecting a job
    st.sidebar.radio(
        "Select a job at your firm:",
        ("other managers", "support intellectuals and scientists, technicians and professionals", "sales representatives and similar")
    )
    
    # Number input for 'g' in the main layout
    st.write("### Skill Gap Adjustment")
    g = st.number_input(
        "Adjust the value of g (Skill gap):",
        key='g',
        step=1,
        min_value=1,  # Avoid division by zero by setting min_value to 1
        max_value=100,
        value=10  # Default value
    )
    
    # Plot Effort Supply dynamically
    w = np.linspace(0.1, 10, 100)  # Positive values for w
    fig = plt.figure(figsize=(5, 5), dpi=100)
    plt.plot(w, 2 * w / g, color='red', label='Effort supply')
    plt.title('Effort Supply Curve')
    plt.xlabel('Wages (w)')
    plt.ylabel('Effort Supply')
    plt.legend()
    
    # Display the plot
    st.pyplot(fig)

st.set_page_config(page_title="UNIT 7. COMPENSATION", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['UNIT 7. COMPENSATION'],  # required
    icons=["book", "book", "people"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "UNIT 7. COMPENSATION":
    UNIT7_1()
