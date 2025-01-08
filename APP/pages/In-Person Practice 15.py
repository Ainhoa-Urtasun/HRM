import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu



def UNIT5_1():

  st.sidebar.header("Settings")
  skill_gaps_input = st.sidebar.text_area("Enter skill gaps (e.g., 0.1, 0.5, 1.0):","")
  try:
    skill_gaps = [float(g.strip()) for g in skill_gaps_input.split("\n") if g.strip()]
  except ValueError:
    st.error("Please enter valid numeric values for skill gaps.")
    skill_gaps = []
  w_probation = st.sidebar.slider("Set probation wage (horizontal line):", 0.0, 100.0, 1.0, 0.1)
  e_values = np.linspace(0, 10, 500)
  fig, ax = plt.subplots(figsize=(8, 6))
  for g in skill_gaps:
    y_values = g * e_values**2
    ax.plot(e_values, y_values, label=f"C(e_i) = {g}e_i^2", linewidth=2)
  ax.axhline(y=w_probation, color='red', linestyle='--', linewidth=2, label=f"w_probation = {w_probation}")
  ax.set_xlabel("Effort (e_i)", fontsize=14)
  ax.set_ylabel("Cost (C(e_i))", fontsize=14)
  ax.set_title("Cost of Effort Function", fontsize=16)
  ax.legend(fontsize=12)
  ax.grid(True)
  st.pyplot(fig)

st.set_page_config(page_title="In-Person Practice 15", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['In-Person Practice 15'],  # required
    icons=["person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == 'In-Person Practice 15':
    UNIT5_1()

