import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():
    st.sidebar.write('Vector of Skills Possessed by the Employee:')
    with st.sidebar.expander("Vector of Skills Possessed by the Employee"):
        s1 = st.number_input("demonstrating willigness to learn",key='s1',min_value=0,max_value=100,step=1)
        s2 = st.number_input("collaborating in teams and networks",key='s2',min_value=0,max_value=100,step=1)
        s3 = st.number_input("working efficiently",key='s3',min_value=0,max_value=100,step=1)
        s4 = st.number_input("taking a proactive approach",key='s4',min_value=0,max_value=100,step=1)

    st.sidebar.write('Vector of Required Skills:')
    with st.sidebar.expander("Vector of Required Skills"):
        s1k = st.number_input("demonstrating willigness to learn",key='s1',min_value=0,max_value=100,step=1)
        s2k = st.number_input("collaborating in teams and networks",key='s2',min_value=0,max_value=100,step=1)
        s3k = st.number_input("working efficiently",key='s3',min_value=0,max_value=100,step=1)
        s4k = st.number_input("taking a proactive approach",key='s4',min_value=0,max_value=100,step=1)
    
    gap = np.sqrt(np.sum((1/np.sqrt(5))*np.array([s1k,s2k,s3k,s4k]) - (1/np.sqrt(5))*np.array([s1,s2,s3,s4])) ** 2))

(1/np.sqrt(5))*np.array([s1,s2,s3,s4]
            
st.set_page_config(page_title="In-Person Practice 12", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['In-Person Practice 12'],  # required
    icons=['people'],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "In-Person Practice 12":
    UNIT4_1()
