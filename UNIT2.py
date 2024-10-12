import streamlit as st
import pandas as pd

def show():
    st.sidebar.header("HR Planning")
    st.text_area('', placeholder="Explain the importance of HR planning")
    
    st.sidebar.header("Input Data for Workforce Planning")
    job_titles = st.sidebar.text_area("Job Titles (comma-separated)", value="Manager, Engineer, Operator")
    job_titles = [title.strip() for title in job_titles.split(",")]

    st.header("Current Workforce")
    current_workforce = {}
    for title in job_titles:
        count = st.number_input(f"Number of {title}s", min_value=0, step=1, value=1, key=f"current_{title}")
        current_workforce[title] = count

    st.header("Projected Workforce Needs")
    projected_workforce = {}
    for title in job_titles:
        count = st.number_input(f"Projected Number of {title}s", min_value=0, step=1, value=1, key=f"projected_{title}")
        projected_workforce[title] = count

    st.header("Workforce Gap Analysis")
    gap_analysis = {title: projected_workforce[title] - current_workforce[title] for title in job_titles}
    gap_df = pd.DataFrame(list(gap_analysis.items()), columns=["Job Title", "Workforce Gap"])
    st.table(gap_df)

    st.header("Strategies for Closing Workforce Gaps")
    st.text_area('', placeholder="Outline strategies to address workforce gaps")
