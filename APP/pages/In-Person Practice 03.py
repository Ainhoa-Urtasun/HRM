import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Practice_03():
  
  with st.sidebar.expander("Cost of employees at your firm from SABI"):
    C2020 = st.number_input("2020",key='C2020',step=1.0)
    C2021 = st.number_input("2021",key='C2021',step=1.0)
    C2022 = st.number_input("2022",key='C2022',step=1.0)
  with st.sidebar.expander("Operating revenue of your firm from SABI"):
    OR2020 = st.number_input("2020",key='OR2020',value=1.0,step=1.0)
    OR2021 = st.number_input("2021",key='OR2021',value=1.0,step=1.0)
    OR2022 = st.number_input("2022",key='OR2022',value=1.0,step=1.0)
  with st.sidebar.expander("Number of employees at your firm from SABI"):
    L2020 = st.number_input("2020",key='L2020',value=1.0,step=1.0)
    L2021 = st.number_input("2021",key='L2021',value=1.0,step=1.0)
    L2022 = st.number_input("2022",key='L2022',value=1.0,step=1.0)

  LP = [OR2020/L2020,OR2021/L2021,OR2022/L2022]
  ULC = [C2020/OR2020,C2021/OR2021,C2022/OR2022]

  fig = plt.figure(figsize=(5,5),dpi=100)
  plt.plot(['2020','2021','2022'],LP,color='red',label='Labor productivity')
  plt.plot(['2020','2021','2022'],ULC,color='blue',label='ULC')
  plt.title('HRM metrics over time')
  plt.legend()
  st.pyplot(fig)

# Set page configuration
st.set_page_config(page_title="In-Person Practice 03", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['In-Person Practice 03'],  # required
    icons=['person'],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == 'In-Person Practice 03':
    Practice_03()

