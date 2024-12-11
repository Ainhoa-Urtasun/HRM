import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt

def Practice_03():
    years = ['2020', '2021', '2022']

    # Sidebar inputs
    with st.sidebar.expander("Cost of employees at your firm from SABI"):
        costs = [st.number_input(year, key=f'C{year}', step=1.0) for year in years]

    with st.sidebar.expander("Operating revenue of your firm from SABI"):
        revenues = [st.number_input(year, key=f'OR{year}', value=1.0, step=1.0) for year in years]

    with st.sidebar.expander("Number of employees at your firm from SABI"):
        employees = [st.number_input(year, key=f'L{year}', value=1.0, step=1.0) for year in years]

    # Calculations
    LP = [revenue / employee for revenue, employee in zip(revenues, employees)]
    ULC = [cost / revenue for cost, revenue in zip(costs, revenues)]

    # Plotting
    fig = plt.figure(figsize=(5, 5), dpi=100)
    plt.plot(years, LP, color='red', label='Labor productivity')
    plt.plot(years, ULC, color='blue', label='ULC')
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



