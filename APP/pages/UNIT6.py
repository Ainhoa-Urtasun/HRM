def UNIT1_4():


    
    st.write(
        '''
        **Employment** refers to the number of employees, including both full-time and part-time workers. 
        **New hires** refers to the number of employees who have recently been recruited and started working at the firm.
        **Separations** refers to the number of employees who leave the firm, either voluntarily (quitting, retiring) 
        or involuntarily (layoffs, dismissals).

        We can also calculate the total employment of the firm at $(t-1)$ and at $(t)$ as well as
        its retention and turnover rates, which are critical HRM metrics.
        '''
    )

    st.latex(r'L_{(t-1)} = L_{1(t-1)}+ L_{2(t-1)} + L_{3(t-1)}')
    st.latex(r'L_{(t)} = L_{1(t)}+ L_{2(t)} + L_{3(t-1)}')
    st.latex(r'\text{Retention} = 100 \times \frac{m_{11(t-1,t)}+m_{22(t-1,t)}+m_{33(t-1,t)}}{L_{(t-1)}}')
    st.latex(r'\text{Turnover} = 100 - \text{Retention}')
    
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
