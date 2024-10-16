import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():
    st.write(
        '''
        Human resource management (HRM) takes on the organization and motivation of employees by implementing HRM practices
        such as job analysis and design, recruitment, HR planning, performance evaluation, training, compensation, 
        and career development. HRM is implemented at the firm level.

        
        The essense of any firm, regardless of its size or legal form of ownership, depends on two important decisions:
        - **What output (good or service) to produce**
        - **How to produce it**
        
        The second decision involves in turn the following specific decisions:
        - What activities the firm needs to complete to produce the output.
        - How to allocate these activities into the factors of production (labor and technology)

        The activities allocated to labor (employees) are called **work activities** and HRM organizes and motivates
        employees to perform **work activities** efficiently and effectively.

        Firms are classified into industries depending on the output they produce and jobs are classified into occupations depending on
        the work activities they entail. The North American Industry Classification System (NAICS) provides a standard classification
        of firms into industries and the Standard Occupational Classification (SOC) provides
        a standard classification of jobs into occupations.
        '''
    )

    st.text_input("Enter the name of the firm from SABI")
    st.text_input("Enter the 2-digit NAICS code and title of the firm from SABI")
    st.components.v1.iframe("https://www.unavarra.es/biblioteca?languageId=1", width=800, height=600, scrolling=True)

    st.write("Enter 4 work activities ($A_i$) from O*NET:")
    activity1 = st.text_input("$A_1$")
    activity2 = st.text_input("$A_2$")
    activity3 = st.text_input("$A_3$")
    activity4 = st.text_input("$A_4$")
    st.components.v1.iframe("https://www.onetonline.org/find/descriptor/browse/4.A", width=800, height=600, scrolling=True)
  
def UNIT1_2():
    with st.expander("Show the notation for the **Human Resource Management (HRM)** course"):
        st.write("- $L_1$ number of employees in job $J_1$ at the firm")
        st.write("- $L_2$ number of employees in job $J_2$ at the firm")
        st.write("- $L_3$ number of employees in job $J_3$ at the firm")
        st.write("- $K$ technology at the firm")
        st.write("- $Q = L_1^{e_1}K$"
        st.write("- $A_1, A_2, A_3, A_4$ work activities to be performed by employees")
        st.write("- $S_1, S_2, S_3, S_4, S_5, S_6$ skills to be possessed by employees")

    st.write("Use the section above to view the notation for the **Human Resource Management (HRM)** course.")

def UNIT1_3():
    st.write("""
        Both metrics are essential for HRM. To calculate them the following two items from the Income Statement are needed:
        **Operating revenue** and **Cost of employees**. 
        The **Cost of employees**, along with **Depreciation**, are part of **Operating expenses**, 
        that substracted from **Operating revenue** results in 
        **Earnings Before Interests and Taxes (EBIT)**."""
    )

    st.components.v1.iframe("https://www.unavarra.es/biblioteca?languageId=1", width=800, height=600, scrolling=True)
  
    cost_input = st.sidebar.text_input("Cost of Employees (comma-separated for 2019, 2020, 2021):", "0,0,0")
    revenue_input = st.sidebar.text_input("Operating Revenue (comma-separated for 2019, 2020, 2021):", "1,1,1")
    employees_input = st.sidebar.text_input("Number of Employees (comma-separated for 2019, 2020, 2021):", "1,1,1")

    costs = np.fromstring(cost_input, sep=',')
    revenues = np.fromstring(revenue_input, sep=',')
    employees = np.fromstring(employees_input, sep=',')

    labor_productivity = revenues / employees / 1000  # Convert to thousands
    unit_labor_cost = costs / revenues
        
    df = pd.DataFrame({
        "Year": ["2019", "2020", "2021"],
        "Labor Productivity (in thousands)": labor_productivity,
        "Unit Labor Cost": unit_labor_cost
    })

    fig, ax = plt.subplots()
    ax.plot(["2019", "2020", "2021"], labor_productivity, marker='x', label='Labor Productivity')
    ax.plot(["2019", "2020", "2021"], unit_labor_cost, marker='o', label='Unit Labor Cost')        
    ax.set_xlabel('Year')
    ax.set_ylabel('Metrics')
    ax.set_title("Trends in HRM metrics")
    ax.legend()
    st.pyplot(fig)

def UNIT1_4():
    st.write(
        """Both labor productivity and ULC significantly impact a firm's profitability, 
        particularly in terms of Earnings Before Interest and Taxes (EBIT). 
        Firms often make decisions aimed at maximizing profits, 
        which is the focus of this section:
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

    L1 = st.number_input("Supply of employees in job $J_1$ at the firm", value=1, step=1)
    L2 = st.number_input("Supply of employees in job $J_2$ at the firm", value=1, step=1)
    L3 = st.number_input("Supply of employees in job $J_3$ at the firm", value=1, step=1)

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
                "Demand of employees in job $J_1$ at the firm": [L1_new],
                "Demand of employees in job $J_2$ at the firm": [L2_new],
                "Demand of employees in job $J_3$ at the firm": [L3_new],
                "EBIT": [new_value]
            })
            st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>Updated Values After First Iteration</h3>", unsafe_allow_html=True)
            st.table(result)

# Set page configuration
st.set_page_config(page_title="UNIT1", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["HRM", "Notation for the Course", "Labor Productivity and Unit Labor Cost (ULC)", "EBIT Optimization"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "HRM":
    UNIT1_1()
elif selected == "Notation for the Course":
    UNIT1_2()
elif selected == "Labor Productivity and Unit Labor Cost (ULC)":
    UNIT1_3()
elif selected == "EBIT Optimization":
    UNIT1_4()

