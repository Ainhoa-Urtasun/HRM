import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():

    st.write(
        '''
        Performance evaluation refers to assessing how well employees perform within the firm. 
        Performance can be evaluated on average or for each specific employee, with the latter being more challenging 
        but also more meaningful.

        A typical average performance metric is labor productivity.
        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.text_input("Write here the labor productivity of your firm using the latest information provided by [SABI](https://www.unavarra.es/biblioteca?languageId=1):")

def UNIT4_2():
    
    st.write(
        '''
        A more meaningful but also more challenging way to evaluate performance is to assess 
        how well each employee performs within the firm. If done properly, 
        this allows the firm to understand each employee's contribution to its value 
        and to motivate them to improve their performance.

        Here, we present several alternative metrics for evaluating employee performance. Given our production function's 
        dependence on the individual effort exerted by each employee, one such metric could be the output elasticity of effort.

        '''
    )

    st.latex(
         r'''
        \alpha_i = \frac{\partial f(e_1, e_2, \dots, e_i, \dots, e_L)}{\partial e_i} \cdot \frac{e_i}{f(e_1, e_2, \dots, e_i, \dots, e_L)}
        '''
    )

    st.write(
        '''
        This output elascticity indicates the percentage change in the output
        the firm produces when employee $i$ exerts 1% more effort.
        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.text_input('From [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) choose one occupation for which you wish to post a job:')
    st.text_input('For that job posting, offer a salary equal to the median monthly gross income in EUR for that occupation as reported in [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence):')
    st.text_input('Explain why you might end up recruiting the wrong job candidates:')

def UNIT5_3():
    st.write(r"The cost of effort for each employee or job candidate is defined as:")
    st.write(r"$$C(e) = (100 - S)e^2$$")
    st.write(r"where:")
    st.write(r" - \( C(e) \) is the total cost of effort,")
    st.write(r" - \( e \) represents the level of effort exerted,")
    st.write(r" - \( S \) denotes the skill or credential level required to apply for the job.")

    st.write(r"Assuming \( S = 99 \), indicating a high-skill candidate, then their cost of effort becomes:")
    st.write(r"$$C(e) = e^2$$")
    st.write(r"This lower cost reflects that the high-skill candidate possesses the necessary skill abundantly, making effort less costly for them.")

    st.write(r"For a low-skill candidate, assuming \( S = 0 \), the cost of effort is:")
    st.write(r"$$C(e) = 100 e^2$$")
    st.write(r"This higher cost implies that it would be more expensive for the low-skill candidate to exert the same level of effort as the high-skill candidate.")

    st.write(r"The company offers a salary of 4,000, expecting a target effort level of \( e = 200 \).")
    st.write(r"Under this salary and effort expectation, a high-skill candidate (\( S = 99 \)) is willing to exert the required effort, as their cost of effort \( C(e) = e^2 = 200^2 = 40,000 \) is feasible.")
    st.write(r"In contrast, a low-skill candidate (\( S = 0 \)) would face a prohibitive cost of \( C(e) = 100 \times 200^2 = 4,000,000 \) and thus would not apply.")
    st.write(r"The challenge remains: how to measure and control for the actual effort exerted by candidates to ensure that the required skill level aligns with job expectations.")

st.set_page_config(page_title="UNIT4", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Average performance evaluation",'Employee performance evaluation'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Average performance evaluation":
    UNIT4_1()
elif selected == "Employee performance evaluation":
    UNIT4_2()
