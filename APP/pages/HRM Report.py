import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def report():
  user_text = st.text_area("Your text here:", placeholder="Type something...")

st.set_page_config(page_title="HRM Report", layout="wide")




