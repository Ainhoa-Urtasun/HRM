import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():
    st.write(
        '''Firms make two important decisions, **what to produce** and **how to produce it**. The **what to produce** decision refers to the output (good or service).
        The **how to produce it** decision, on the other hand, refers to the activities to be performed and who, labor or technology, performs these activities. 
        We refer to the activities that labor (employees) must complete as **work activities**. As part of the **how to produce it** decision, firms also decide how 
        to group these **work activities** into jobs or occupations and how many employees are needed for each occupation. As firms are classified into industries 
        depending on the output they produce, employees are classified into occupations depending on the work activities they perform. 
        [The North American Industry Classification System (NAICS)](https://www.census.gov/naics/) classifies firms into industries depending on the type of output they produce
        and the [Standard Occupational Classification (SOC)](https://www.bls.gov/soc/2018/major_groups.htm) classifies employees into occupations. 
        To streamline our analysis, this course focuses on three occupations.'''
    )
    
def UNIT1_2():
    with st.expander("Show the notation for the **Human Resource Management (HRM)** course"):
        st.write("- $L_{1}$ number of employees in occupation 1 at the firm")
        st.write("- $L_{2}$ number of employees in occupation 2 at the firm")
        st.write("- $L_{3}$ number of employees in occupation 3 at the firm")
        st.write("- $K$ technology at the firm")
        st.write("- $A_1$, $A_2$, $A_3$, $A_4$ work activities to be performed by employees")
        st.write("- $S_1$, $S_2$, $S_3$, $S_4$, $S_5$, $S_6$ skills to be possessed by employees")

    st.write("Use the section above to view the notation for the **Human Resource Management (HRM)** course.")

def UNIT1_3():
    st.write("""
        Both metrics are essential for HRM. To calculate them the following two items from the Income Statement are needed: **Operating revenue**, **Cost of employees**. 
        The **Cost of employees**, along with **Depreciation**, is part of **Operating expenses**, that substracted from **Operating revenue** results in 
        **Earnings Before Interests and Taxes (EBIT)**."""
    )

    st.write("""
        We are going to practice calculating both labor productivity and unit labor cost (ULC) using the SABI database at the UPNA library."""
    )

    st.components.v1.iframe("https://www.unavarra.es/biblioteca?languageId=1", width=800, height=600, scrolling=True)

    
    cost_input = st.sidebar.text_input("Cost of Employees (comma-separated for 2019, 2020, 2021):", "0,0,0")
    revenue_input = st.sidebar.text_input("Operating Revenue (comma-separated for 2019, 2020, 2021):", "1,1,1")
    employees_input = st.sidebar.text_input("Number of Employees (comma-separated for 2019, 2020, 2021):", "1,1,1")

    costs = np.fromstring(cost_input, sep=',')
    revenues = np.fromstring(revenue_input, sep=',')
    employees = np.fromstring(employees_input, sep=',')
        
    unit_labor_cost = costs / revenues
    labor_productivity = revenues / employees / 1000  # Convert to thousands
    
    df = pd.DataFrame({
        "Year": ["2019", "2020", "2021"],
        "Unit Labor Cost": unit_labor_cost,
        "Labor Productivity (in thousands)": labor_productivity
    })

    fig, ax = plt.subplots()
    ax.plot(["2019", "2020", "2021"], unit_labor_cost, marker='o', label='Unit Labor Cost')
    ax.plot(["2019", "2020", "2021"], labor_productivity, marker='x', label='Labor Productivity')    
    ax.set_xlabel('Year')
    ax.set_ylabel('Metrics')
    ax.set_title("Trends in Unit Labor Cost and Labor Productivity")
    ax.legend()
    st.pyplot(fig)

def UNIT1_4():
    st.write(
        """Both labor productivity and unit labor cost (ULC) significantly impact a firm's profitability, 
        particularly in terms of Earnings Before Interest and Taxes (EBIT). Firms often make decisions aimed at maximizing profits, 
        which is the focus of this section
        """
    )
    st.latex(r'''
        EBIT = p\left(L_{1}^{e_{1}} \cdot L_{2}^{e_{2}} \cdot L_{3}^{e_{3}} \cdot K^{1-e_{1}+e_{2}-e_{3}}\right) - \left(w_{1} L_{1} + w_{2} L_{2} + w_{3} L_{3}\right) - rK
    ''')
    
    st.write("Where:")
    st.write("- $p$ is the price of the output")
    st.write("- $w_{1} L_{1} + w_{2} L_{2} + w_{3} L_{3}$ represents cost of employees")
    st.write("- $rK$ represents depreciation")

    st.write(
        "The objective is to determine the optimal values of $(L_{1}, L_{2}, L_{3})$ that maximize EBIT. "
        "We can apply gradient ascent to iteratively update the input values, moving in the direction of the gradient. "
        "The gradient indicates the direction that maximizes the objective function:"
    )
    st.latex(r'''
        (L_{1}, L_{2}, L_{3})_{\text{new}} = (L_{1}, L_{2}, L_{3})_{\text{old}} + \eta \cdot \nabla EBIT
    ''')

    st.write("Where:")
    st.write("- $\\eta$ is the learning rate (which determines the size of the steps),")
    st.write("- $\\nabla EBIT$ is the gradient of the EBIT function with respect to $(L_{1}, L_{2}, L_{3})$, defined as:")

    st.latex(r'''
    \nabla EBIT = \left( \frac{\partial EBIT}{\partial L_{1}}, \frac{\partial EBIT}{\partial L_{2}}, \frac{\partial EBIT}{\partial L_{3}} \right)
    ''')

    st.write("By calculating the gradient and updating the input values iteratively, we aim to find the optimal combination "
             "of labor and capital that maximizes EBIT, enhancing overall firm profitability.")

    L1 = st.number_input("Supply of employees in occupation 1 at the firm", value=1, step=1)
    L2 = st.number_input("Supply of employees in occupation 2 at the firm", value=1, step=1)
    L3 = st.number_input("Supply of employees in occupation 3 at the firm", value=1, step=1)

    def EBIT(L1, L2, L3):
        return 120 * L1**0.2 * L2**0.5 * L3**0.1 - 5 * (L1 + L2 + L3) - 1

    def gradient_L1(L1, L2, L3):
        return 120 * 0.2 * L1**(-0.8) * L2**0.5 * L3**0.1  - 5

    def gradient_L2(L1, L2, L3):
        return 120 * 0.5 * L1**0.2 * L2**(-0.5) * L3**0.1 - 5

    def gradient_L3(L1, L2, L3):
        return 120 * 0.1 * L1**0.2 * L2**0.5 * L3**(-0.9) - 5

    initial_EBIT = EBIT(L1, L2, L3)
    st.markdown(f"<h3 style='text-align: center; color: #FF5733;'>Starting EBIT: {initial_EBIT:.2f}€</h3>", unsafe_allow_html=True)

    if st.button("First iteration"):
        L1_new = L1 + 0.02 * gradient_L1(L1, L2, L3)
        L2_new = L2 + 0.02 * gradient_L2(L1, L2, L3)
        L3_new = L3 + 0.02 * gradient_L3(L1, L2, L3)

        L1_new = round(L1_new)
        L2_new = round(L2_new)
        L3_new = round(L3_new)

        if L1_new <= 0 or L2_new <= 0 or L3_new <= 0:
            st.error("The updated values of L1, L2, and L3 must be positive. Please adjust the initial values or the learning rate.")
        else:
            new_value = EBIT(L1_new, L2_new, L3_new)
            result = pd.DataFrame({
                "Demand of employees in occupation 1 at the firm": [L1_new],
                "Demand of employees in occupation 2 at the firm": [L2_new],
                "Demand of employees in occupation 3 at the firm": [L3_new],
                "EBIT": [new_value]
            })
            st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>Updated Values After First Iteration</h3>", unsafe_allow_html=True)
            st.table(result)

# Set page configuration
st.set_page_config(page_title="UNIT1", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Industries and Occupations", "Notation for the Course", "Labor Productivity and Unit Labor Cost (ULC)", "EBIT Optimization"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Industries and Occupations":
    UNIT1_1()
elif selected == "Notation for the Course":
    UNIT1_2()
elif selected == "Labor Productivity and Unit Labor Cost (ULC)":
    UNIT1_3()
elif selected == "EBIT Optimization":
    UNIT1_4()

