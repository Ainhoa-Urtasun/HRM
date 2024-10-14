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
    with st.expander("Show the notation for the course"):
        st.write("- $L_{1}$ number of employees in occupation 1 at the firm")
        st.write("- $L_{2}$ number of employees in occupation 2 at the firm")
        st.write("- $L_{3}$ number of employees in occupation 3 at the firm")
        st.write("- $K$ technology at the firm")
        st.write("- $A_1$, $A_2$, $A_3$, $A_4$ work activities to be performed by employees")
        st.write("- $S_1$, $S_2$, $S_3$, $S_4$, $S_5$, $S_6$ skills to be possessed by employees")

    st.write("Use the section above to view the notation for the course.")

def UNIT1_3():
    st.title('Earnings Before Interests and Taxes (EBIT)')
    st.write("""
        Earnings Before Interest and Taxes (EBIT) is a measure of a company's profitability 
        that excludes interest and income tax expenses. It represents the profit generated 
        from the company's core business operations, providing insight into how effectively 
        the company is being managed and its ability to generate operating profits. 
        EBIT is often used to compare the performance of companies within the same industry, 
        as it removes the effects of financing and tax structures, allowing for a clearer 
        analysis of operational efficiency."""
    )

    st.markdown("""
    | **Income Statement**                | **Amount** |
    |:------------------------------------|-----------:|
    | + Operating Revenue (Turnover)      |    $X,XXX  |
    | - Operating Expenses                |    $X,XXX  |
    | **= EBIT (Operating P/L)**          | **$X,XXX** |
    """)

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
    st.title("Cost of Employees")
    st.write(
        """Employees contribute to the firm's profits at a cost. The Income Statement records only a portion of all this cost, 
        under the category of **cost of employees**. The most significant component of the cost of employees is compensation, 
        but recruitment and training costs may also be included. Another important cost, not recorded in the Income Statement, is the **cost of effort**. 
        The cost of effort refers to the opportunity cost for the employee to exert effort, which has significant implications for their motivation. HR 
        managers must carefully manage both types of costs to maintain employee performance and profitability."""
    )

def UNIT1_5():
    st.title("EBIT Optimization")
    st.latex(r'''
        EBIT = p\left(L_{11}^{e_{11}} \cdot L_{17}^{e_{17}} \cdot L_{51}^{e_{51}} \cdot K^{1-e_{11}+e_{17}-e_{51}}\right) - \left(w_{11} L_{11} + w_{17} L_{17} + w_{51} L_{51}\right) - rK
    ''')
    st.write(
        "where $p$ is the price of the output, "
        "$w_{11} L_{11} + w_{17} L_{17} + w_{51} L_{51}$ is the total cost of employees."
        "$rK$ is the cost of capital."
    )
    st.write(
        "The objective is to determine the optimal values of $(L_{11}, L_{17}, L_{51})$ that maximize EBIT. "
        "We can apply gradient ascent to iteratively update the input values, moving in the direction of the gradient. "
        "The gradient indicates the direction that maximizes the objective function:"
    )
    st.latex(r'''
        (L_{11}, L_{17}, L_{51})_{\text{new}} = (L_{11}, L_{17}, L_{51})_{\text{old}} + \eta \cdot \nabla EBIT
    ''')

    st.write("Where:")
    st.write("- $\\eta$ is the learning rate (which determines the size of the steps),")
    st.write("- $\\nabla EBIT$ is the gradient of the EBIT function with respect to $(L_{11}, L_{17}, L_{51})$, defined as:")

    st.latex(r'''
    \nabla EBIT = \left( \frac{\partial EBIT}{\partial L_{11}}, \frac{\partial EBIT}{\partial L_{17}}, \frac{\partial EBIT}{\partial L_{51}} \right)
    ''')

    st.write("By calculating the gradient and updating the input values iteratively, we aim to find the optimal combination "
             "of labor and capital that maximizes EBIT, enhancing overall firm profitability.")

    L11 = st.number_input("Supply of managers", value=1, step=1)
    L17 = st.number_input("Supply of engineers", value=1, step=1)
    L51 = st.number_input("Supply of operators", value=1, step=1)

    def EBIT(L11, L17, L51):
        return 120 * L11**0.2 * L17**0.5 * L51**0.1 - 5 * (L11 + L17 + L51) - 1

    def gradient_L11(L11, L17, L51):
        return 120 * 0.2 * L11**(-0.8) * L17**0.5 * L51**0.1  - 5

    def gradient_L17(L11, L17, L51):
        return 120 * 0.5 * L11**0.2 * L17**(-0.5) * L51**0.1 - 5

    def gradient_L51(L11, L17, L51):
        return 120 * 0.1 * L11**0.2 * L17**0.5 * L51**(-0.9) - 5

    initial_EBIT = EBIT(L11, L17, L51)
    st.markdown(f"<h3 style='text-align: center; color: #FF5733;'>Starting EBIT: {initial_EBIT:.2f}€</h3>", unsafe_allow_html=True)

    if st.button("First iteration"):
        L11_new = L11 + 0.02 * gradient_L11(L11, L17, L51)
        L17_new = L17 + 0.02 * gradient_L17(L11, L17, L51)
        L51_new = L51 + 0.02 * gradient_L51(L11, L17, L51)

        L11_new = round(L11_new)
        L17_new = round(L17_new)
        L51_new = round(L51_new)

        if L11_new <= 0 or L17_new <= 0 or L51_new <= 0:
            st.error("The updated values of L11, L17, and L51 must be positive. Please adjust the initial values or the learning rate.")
        else:
            new_value = EBIT(L11_new, L17_new, L51_new)
            result = pd.DataFrame({
                "Demand of managers": [L11_new],
                "Demand of engineers": [L17_new],
                "Demand of operators": [L51_new],
                "EBIT": [new_value]
            })
            st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>Updated Values After First Iteration</h3>", unsafe_allow_html=True)
            st.table(result)

# Set page configuration
st.set_page_config(page_title="UNIT1", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Industries and Occupations", "Notation for the Course", "Earnings Before Interests and Taxes (EBIT)", "Cost of Employees", "EBIT Optimization"],  # required
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
elif selected == "Earnings Before Interests and Taxes (EBIT)":
    UNIT1_3()
elif selected == "Cost of Employees":
    UNIT1_4()
elif selected == "EBIT Optimization":
    UNIT1_5()

