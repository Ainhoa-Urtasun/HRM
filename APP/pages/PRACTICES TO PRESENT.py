import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT0_1():
    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practices Overview</h3>", unsafe_allow_html=True)
    st.write(
        '''
        In this course, students will complete **25 Practices**, each contributing 1% to their final grade. 
        These practices are divided into two main types and are completed regularly during class sessions:
        
        - **Test & Quiz Practices**: Exam-like questions for each unit.
        - **Interactive Practices**: Hands-on tasks completed through an app, with students presenting their findings 
          out loud to enhance their communication skills. Students can work individually or in pairs.

        Students will present the **interactive practices** in two stages:
        - **Mid-Semester Presentations**: Practices 3, 6, 9, and 12.
        - **End-of-Semester Presentations**: Practices 15, 18, 21, and 24.

        Practice 25, at the end of the semester, will evaluate the **cohesiveness** and **connection** between all the interactive practices presented. This ensures students integrate their learnings effectively and present a coherent narrative.

        The table below summarizes the practices by unit and type:
        '''
    )

    st.markdown(
        '''
        | Unit    |  Test & Quiz Practices   | Interactive Practices                       |
        |---------|--------------------------|--------------------------------------------|
        | Unit 1  | 1, 2                     | 3                                          |
        | Unit 2  | 4, 5                     | 6                                          |  
        | Unit 3  | 7, 8                     | 9                                          |       
        | Unit 4  | 10, 11                   | 12 (mid-semester presentations: 3, 6, 9, 12)|    
        | Unit 5  | 13, 14                   | 15                                         |
        | Unit 6  | 16, 17                   | 18                                         |  
        | Unit 7  | 19, 20                   | 21                                         |       
        | Unit 8  | 22, 23                   | 24 (end-semester presentations: 15, 18, 21, 24)|    
        | Final   |                          | 25 (evaluates cohesiveness and connection) |

        **Supporting Resources**:
        - [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) from CEDEFOP (European Centre for the Development of Vocational Training)
        - [SABI](https://www.unavarra.es/biblioteca?languageId=1) from UPNA library
        '''
    )

st.set_page_config(page_title="Practices Overview", layout="wide")

# Directly call the function since there's only one menu option for now.
UNIT0_1()
