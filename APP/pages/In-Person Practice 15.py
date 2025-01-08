import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu



def UNIT5_1():

  # Sidebar configuration
  st.sidebar.header("Settings")

  # Add or modify cost functions
  cost_functions = st.sidebar.text_area(
      "Enter cost functions (e.g., 0.1*x**2, 0.2*x**2):",
      "0.1*x**2\n0.2*x**2\n0.5*x**2"
  ).split("\n")

  # Set horizontal line (w_probation)
  w_probation = st.sidebar.slider("Set probation wage (horizontal line):", 0.0, 5.0, 1.0, 0.1)

  # Generate x values
  e_values = np.linspace(0, 10, 500)

  # Plot configuration
  fig, ax = plt.subplots(figsize=(8, 6))

  # Plot each cost function
  for i, func in enumerate(cost_functions):
      try:
          # Parse the function and compute y values
          y_values = [eval(func.replace("x", str(e))) for e in e_values]
          ax.plot(e_values, y_values, label=f"C(e_i) = {func}", linewidth=2)
      except Exception as e:
          st.error(f"Error in function {func}: {e}")

  # Plot horizontal line (w_probation)
  ax.axhline(y=w_probation, color='red', linestyle='--', linewidth=2, label=f"w_probation = {w_probation}")

  # Plot aesthetics
  ax.set_xlabel("Effort (e_i)", fontsize=14)
  ax.set_ylabel("Cost (C(e_i))", fontsize=14)
  ax.set_title("Cost of Effort Functions", fontsize=16)
  ax.legend(fontsize=12)
  ax.grid(True)

  # Display the plot
  st.pyplot(fig)

  # Instructions for user
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

