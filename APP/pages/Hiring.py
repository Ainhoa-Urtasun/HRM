import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def hiring():

  st.sidebar.header("Designing probation")
  skill_gaps_input = st.sidebar.text_area("Enter several possible skill gaps (each between 0 and 100). Write one per line and press Enter after each):","")
  try:
    skill_gaps = [float(g.strip()) for g in skill_gaps_input.split("\n") if g.strip()]
  except ValueError:
    st.error("Please enter valid numeric values for skill gaps.")
    skill_gaps = []
  w_probation = st.sidebar.slider("Set probation wage (horizontal line):", 0, 5000, 1, 1)
  
  st.text_area("", placeholder="Explain signaling as an HRM practice")
  st.text_area("", placeholder="Explain screening as an HRM practice")
  st.text_area("", placeholder="Explain how probation functions as both a signalling and screening mechanism")
  st.text_area("", placeholder="Explain how your firm should design probation to attract job candidates with a small skill gap")

  e_values = np.linspace(0, 10, 500)
  fig, ax = plt.subplots(figsize=(8, 6))
  for g in skill_gaps:
    y_values = g * e_values**2
    ax.plot(e_values, y_values, label=f"Cost of effort if skill gap is: {g}", linewidth=2)
  ax.axhline(y=w_probation, color='red', linestyle='--', linewidth=2, label=f"Probation wage = {w_probation}")
  ax.set_xlabel("$e_i$", fontsize=14)
  ax.legend(fontsize=12)
  ax.grid(True)
  st.pyplot(fig)

st.set_page_config(page_title="Hiring", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['Hiring'],  # required
    icons=["person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == 'Hiring':
    hiring()
