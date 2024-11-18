import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT7_1():
 st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 22 </h3>", unsafe_allow_html=True)
 st.sidebar.radio("Select a job at your firm:",("other managers", "support intellectuals and scientists, technicians and professionals", "sales representatives and similar"))
 with st.sidebar.expander("Skill gap"):
   g = st.number_input("g",key='g',step=1,min_value=0,max_value=100)
   w = np.linspace(0.1,10,100)
   fig = plt.figure(figsize=(5,5),dpi=100)
   plt.plot(w,2*w/g,color='red',label='Effort supply')
   plt.legend()
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
