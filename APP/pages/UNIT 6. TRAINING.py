import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT6_1():

    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 19 </h3>", unsafe_allow_html=True)
    with st.sidebar.expander("Trained employee's skill"):
        t0 = st.number_input("-1", key="t0", step=1)
        t1 = st.number_input("+1", key="t1", step=1)
    with st.sidebar.expander("Non-trained employee's skill"):
        n0 = st.number_input("-1", key="n0", step=1)
        n1 = st.number_input("+1", key="n1", step=1)
    fig = plt.figure(figsize=(5,5),dpi=100)
    plt.plot(['-1','+1'],[t0,t1],color='red',label="Trained employee's skill")
    plt.plot(['-1','+1'],[n0,n1],color='blue',label="Non-trained employee's skill")
    plt.plot(['-1','+1'],[t0,t0+(n1-n0)],color='green',ls='-.',label='Counterfactual')
    plt.title('Evaluating training')
    plt.legend()
    st.pyplot(fig)
  
st.set_page_config(page_title="UNIT 6. Training", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['UNIT 6. TRAINING'],  # required
    icons=["person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "UNIT 6. TRAINING":
    UNIT6_1()
