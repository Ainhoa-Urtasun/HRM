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

    st.write("Enter 4 work activities ($W_i$) from O*NET:")
    workactivity1 = st.text_input("$W_1$")
    workactivity2 = st.text_input("$W_2$")
    workactivity3 = st.text_input("$W_3$")
    workactivity4 = st.text_input("$W_4$")
    st.components.v1.iframe("https://www.onetonline.org/find/descriptor/browse/4.A", width=800, height=600, scrolling=True)
  
def UNIT1_2():
    with st.expander("Show the notation for the **Human Resource Management (HRM)** course"):
        st.write("- $L_1$ number of employees in job $J_1$ at the firm")
        st.write("- $L_2$ number of employees in job $J_2$ at the firm")
        st.write("- $L_3$ number of employees in job $J_3$ at the firm")
        st.write("- $K$ technology at the firm")
        st.write("- $Q = AL_1^{e_1}L_2^{e_2}L_3^{e_3}K$ Cobb-Douglas production function of the firm")
        st.write("- $W_1, W_2, W_3, W_4$ work activities to be performed by employees")
        st.write("- $S_1, S_2, S_3, S_4, S_5, S_6$ skills to be possessed by employees")

    st.write("Use the section above to view the notation for the **Human Resource Management (HRM)** course.")

def UNIT1_3():
    st.latex(r'Q = A \cdot L_1^{e_1} \cdot L_2^{e_2} \cdot L_3^{e_3} \cdot K')

    st.write("""
    Where:
    - $Q$ is the total output
    - $A$ is multi-factor productivity (TFP), which accounts for all factors of production efficiency other than employees and technology
    - $L_1, L_2, L_3$ are number of employees in 3 different jobs at the firm
    - $e_1, e_2, e_3$ are the output elasticities of each job
    - $K$ is technology
    """)

    st.write("""
    The output elasticities of each type of job ($e_1$, $e_2$, $e_3$) represent the contribution of each job type to the overall performance of the firm. 
    These elasticities measure how much output changes in response to a 1% change in the number of employees in each job type, holding other factors constant. 
    Jobs with higher output elasticities contribute more to the firm's production. 

    Output elasticities are closely linked to labor productivity because they reflect how effectively labor in each job type is transformed into output. 
    Therefore, they are also related to the effort exerted by employees, as more effort can increase the productivity of labor in each job, amplifying its contribution to the firm’s success.
    """)


def UNIT1_4():
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


# Set page configuration
st.set_page_config(page_title="UNIT1", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["HRM", "Notation for the Course", "Output Elasticity of Labor", "Labor Productivity and Unit Labor Cost (ULC)"],  # required
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
elif selected == "Output Elasticity of Labor":
    UNIT1_3()
elif selected == "Labor Productivity and Unit Labor Cost (ULC)":
    UNIT1_4()

