import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():
  
  st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 3 </h3>", unsafe_allow_html=True)

  st.write(
    '''
    - [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) from CEDEFOP (European Centre for the 
    Development of Vocational Training)
    - [SABI](https://www.unavarra.es/biblioteca?languageId=1) from the library at UPNA

    Choose your firm:
    1. Access the SABI database through the UPNA Library
    2. In 'Personalizar' then 'Opciones Generales', change the language to English
    3. Firm qualification based on **Employees** criteria>
      - Minimum lastest number of employees of 750
      - Employees' segmentation in Spain (in 2023):
      - Other managers
      - Support intellectuals and scientists, technicians and professionals
      - Administrative employees
      - At least 10 women
    4. View list of results
    5. Select one firm from the firms that qualify
    '''
  )

  st.text_input('', placeholder='Write here the name of your firm')
  st.text_input('Select your firm and then **Overview** under **Industry & overview**',placeholder="Write here your firm's NACE Rev. 2 Primary Code and English trade description")
                                                                                                   
  with st.sidebar.expander("Cost of employees at your firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1)"):
    C2020 = st.number_input("2020",key='C2020',step=1.0)
    C2021 = st.number_input("2021",key='C2021',step=1.0)
    C2022 = st.number_input("2022",key='C2022',step=1.0)
  with st.sidebar.expander("Operating revenue of your firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1)"):
    OR2020 = st.number_input("2020",key='OR2020',value=1.0,step=1.0)
    OR2021 = st.number_input("2021",key='OR2021',value=1.0,step=1.0)
    OR2022 = st.number_input("2022",key='OR2022',value=1.0,step=1.0)
  with st.sidebar.expander("Number of employees at your firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1)"):
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
st.set_page_config(page_title="UNIT 1. HUMAN RESOURCE MANAGEMENT (HRM)", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['UNIT 1 HUMAN RESOURCE MANAGEMENT (HRM)'],  # required
    icons=['person'],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == 'UNIT 1 HUMAN RESOURCE MANAGEMENT (HRM)':
    UNIT1_1()

