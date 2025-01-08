import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu



def UNIT5_1():

  st.sidebar.header("Settings")
  g = st.sidebar.slider("Set skill gap (g):", 0.1, 5.0, 1.0, 0.1)
  w_probation = st.sidebar.slider("Set probation wage (horizontal line):", 0.0, 5.0, 1.0, 0.1)
  e_values = np.linspace(0, 10, 500)
  y_values = g * e_values**2
  fig, ax = plt.subplots(figsize=(8, 6))
  ax.plot(e_values, y_values, label=f"C(e_i) = {g}e_i^2", color='blue', linewidth=2)
  ax.axhline(y=w_probation, color='red', linestyle='--', linewidth=2, label=f"w_probation = {w_probation}")
  ax.set_xlabel("Effort (e_i)", fontsize=14)
  ax.set_ylabel("Cost (C(e_i))", fontsize=14)
  ax.set_title("Cost of Effort Function", fontsize=16)
  ax.legend(fontsize=12)
  ax.grid(True)
  st.pyplot(fig)
  st.markdown(
      "### Instructions:\n"
      "1. Enter cost functions as mathematical expressions in terms of \(x\), one per line.\n"
      "2. Adjust the probation wage (horizontal line) using the slider.\n"
      "3. The graph will update automatically."
  )

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

