import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT5_1():

    st.write(
        '''
        Employment refers to the number of employees, including both full-time and part-time workers. 
        If we have information of employment in a firm at the job level, 
        we can calculate the total employment of the firm at $(t-1)$ and at $(t)$ as follows,
        assuming $N$ jobs both at $t-1$ and $t$:
        '''
    )

    st.latex(r'L_{(t-1)} = L_{1(t-1)}+ L_{2(t-1)} + ... + L_{N(t-1)}')
    st.latex(r'L_{(t)} = L_{1(t)}+ L_{2(t)} + ...+ L_{N(t-1)}')

    st.write(
        '''
        Then if we have information of yearly employment in a firm we can calculate the 
        compound annual growth rate of employment as follows:
        '''
    )

    st.latex(r'''
    \text{CAGR} = \left( \frac{L_{t+k}}{L_{t}} \right)^{\frac{1}{k}} - 1
    ''')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('From [SABI](https://www.unavarra.es/biblioteca?languageId=1) and for your firm, visualize employment:')
    
    employees_input = st.sidebar.text_input("Number of Employees (comma-separated for 2019, 2020, 2021):", "1,1,1")
    employees = np.fromstring(employees_input, sep=',')
        
    df = pd.DataFrame({
        "Year": ["2019", "2020", "2021"],
        "Employment": employees,
    })

    fig, ax = plt.subplots()
    ax.plot(["2019", "2020", "2021"], employees, marker='x', label='Employment')    
    ax.set_xlabel('Year')
    ax.set_ylabel('Metrics')
    ax.set_title("Employment Over Time")
    ax.legend()
    st.pyplot(fig)

def UNIT5_2():
    
    st.write(
        '''
        In recruiting, **asymmetric information** arises because job candidates 
        know more about their skills than the firm does. This can lead to **adverse selection**, 
        where the firm may end up hiring less qualified candidates due to this information gap. 
        Here’s how adverse selection occurs: to attract a pool of candidates, 
        the firm posts a job ad specifying the tasks, required skills, credentials, 
        and salary for the role. Due to limited information about each candidate’s true abilities, 
        the employer offers an average salary for the position. 
        This attracts candidates who meet the listed credentials, but these credentials, 
        while signaling a certain level of qualification, do not fully reveal each candidate's suitability.
    
        However, this average salary might be too low for the 'good' candidates 
        while still appealing to 'wrong' ones, 
        resulting in adverse selection where primarily 'wrong' candidates apply.

        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.text_input('From [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) choose one occupation for which you wish to post a job:')
    st.text_input('For that job posting, offer a salary equal to the median monthly gross income in EUR for that occupation as reported in [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence):')
    st.text_input('Explain why you might end up recruiting the wrong job candidates:')

def UNIT5_3():
    st.write(
    """
    1. **Structured Screening and Testing**: Use tests that assess specific skills, cognitive abilities, or personality traits relevant to the job. Well-designed tests can reveal true abilities and motivations, reducing reliance on self-reported skills.
    
    2. **Probation Periods**: Offer new hires a trial period where they work temporarily before being offered a full-time position. This allows employers to assess actual performance and alignment with the role.
    
    3. **Referral Programs**: Encourage employee referrals, as current employees are likely to recommend qualified candidates who match the company culture. Referrals generally have lower adverse selection risks.
    
    4. **Transparent Job Postings**: Create clear, detailed job descriptions outlining key responsibilities, expectations, and required skills. This transparency helps attract candidates with relevant qualifications, filtering out unsuitable applicants.
    
    5. **Signaling Mechanisms**: Use educational or certification requirements as signals. Candidates with certifications or degrees in relevant fields are more likely to have the necessary skills and commitment.
    
    6. **Performance-based Compensation**: Implement pay structures tied to performance metrics. Performance-based incentives can help attract candidates who are confident in their ability to meet expectations, reducing adverse selection.
    
    7. **Background Checks**: Conduct thorough background and reference checks to validate candidates' past performance, reliability, and honesty, helping identify those likely to underperform.
    
    8. **Job Previews**: Offer realistic job previews during recruitment, showing candidates the challenges and requirements of the role. This helps align expectations and dissuades unsuitable candidates.

    Each of these strategies helps reduce information asymmetry, allowing employers to make more informed decisions and select candidates who are better fits for the organization.
    """
)

def UNIT5_4():
    st.write(r"The cost of effort for each employee or job candidate is defined as:")
    st.latex(
        r'''
        C(e_i) = (100 - S_i)e_i^2
        '''
    )

    st.write(
        '''
        Assuming two job candidates 1 and 2, $S_1 = 99$ and $S_2 = 0$ indicating a high-skill candidate, 
        and a low-skill candidate. The cost of effort of the high-skill candidate is:
        '''
    )
    
    st.latex(r"C(e_1) = e_1^2")
    st.write(
        '''
        This lower cost reflects that the high-skill candidate possesses the necessary skill abundantly, 
        making effort less costly for them.

        For a low-skill candidate, the cost of effort is:
        '''
    )
    
    st.latex(r"C(e_2) = 100 e_2^2")

    st.write(
        '''
        This higher cost implies that it would be more expensive for the low-skill candidate to 
        exert the same level of effort as the high-skill candidate.
        
        The company offers a monthly salary of €10,000, expecting a target effort level of $e^* = 100$.
        
        Under this salary and effort expectation, a high-skill candidate is willing to exert the 
        required effort.
        In contrast, a low-skill candidate would face a prohibitive cost
        and thus would not apply.
        '''
    )

    st.text_input('Identify the strategy that you believe will best facilitate the successful 
    implementation of this final model.')

st.set_page_config(page_title="UNIT5", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Employment","Asymmetric information and adverse selection",'Ways to mitigate adverse selection','Transparent job descriptions'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Employment":
    UNIT5_1()
elif selected == "Asymmetric information and adverse selection":
    UNIT5_2()
elif selected == "Ways to mitigate adverse selection":
    UNIT5_3()
elif selected == 'Transparent job descriptions':
    UNIT5_4()
