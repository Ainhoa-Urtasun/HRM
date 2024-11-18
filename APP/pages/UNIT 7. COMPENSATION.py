import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT7_1():
 
    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 22 </h3>", unsafe_allow_html=True)
    with st.sidebar.expander("Rate of pay per unit of effort as the median monthly gross income from [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence"):
      w = st.number_input("w",key='w',step=1,min_value=0)
    with st.sidebar.expander("Operating revenue of your firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1)"):
      OR2020 = st.number_input("2020",key='OR2020',value=1.0,step=1.0)


  LP = [OR2020/L2020,OR2021/L2021,OR2022/L2022]
  ULC = [C2020/OR2020,C2021/OR2021,C2022/OR2022]

  fig = plt.figure(figsize=(5,5),dpi=100)
  plt.plot(['2020','2021','2022'],LP,color='red',label='Labor productivity')
  plt.plot(['2020','2021','2022'],ULC,color='blue',label='ULC')
  plt.title('HRM metrics over time')
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
