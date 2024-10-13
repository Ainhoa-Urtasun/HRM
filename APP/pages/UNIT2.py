import streamlit as st

def UNIT2_1():
    st.title("O*NET")
    st.markdown(
        "[O*NET Online](https://www.onetonline.org/) is a comprehensive tool for career exploration and job analysis. "
        "It offers detailed descriptions of the tasks, skills, and other attributes required for more than 1,000 jobs, "
        "making it an invaluable resource for job seekers, workforce development professionals, and HR specialists. "
        "By providing standardized information on various job roles, O*NET Online facilitates job analysis and design, "
        "helping users understand the specific demands and characteristics of different occupations."
    )

def UNIT2_2():
    st.title("Work Activities (A)")
    st.write(
        "A **work activity** (A) is an action performed by an individual that results in a specific output. "
        "Jobs are collections of work activities. Every firm transforms inputs into outputs (goods and services). "
        "The nature of these outputs determines both the industry classification of the firm and the work activities its employees must perform. "
        "This highlights the importance of understanding industry classifications. O*NET identifies 41 distinct work activities, "
        "but for simplicity, we focus on 4 working activities (A):"
    )

    work_activities = {
        "WA_1": {
            "name": "Making decisions and solving problems",
            "description": "Analyzing information and evaluating results to choose the best solution and solve problems."
        },
        "WA_2": {
            "name": "Thinking creatively",
            "description": "Developing, designing, or creating new applications, ideas, relationships, systems, or products."
        },
        "WA_3": {
            "name": "Controlling machines and processes",
            "description": "Using control mechanisms or direct physical activity to operate machines or processes."
        },
        "WA_4": {
            "name": "Selling and Influencing Others",
            "description": "Convincing others to buy merchandise or change their minds or actions."
        }
    }

    selected_activity = st.selectbox("Select a Work Activity:", list(work_activities.values()))

    st.write("### Selected Work Activity Details:")
    st.write(f"**Code:** {selected_activity['name']}")
    st.write(f"**Description:** {selected_activity['description']}")


def UNIT2_3():
    st.title("Basic Skills (S)")
    st.write(
        "A **skill** is an ability or competence that an individual possesses. "
        "Employees use their skills to effectively perform work activities. Skills themselves do not directly produce output; "
        "rather, they enable the completion of tasks. There are various classifications of skills. Here, we focus on basic skills as defined by O*NET. "
        "Basic skills are developed capacities that facilitate learning and the rapid acquisition of knowledge."
    )

    basic_skills_data = {
        "Code": [S_1, S_2, S_3, S_4, S_5, S_6],
        "Skill": [
            "Active listening",
            "Mathematics",
            "Reading comprehension",
            "Science",
            "Speaking",
            "Writing"
        ],
        "Description": [
            "Giving full attention to what other people are saying, taking time to understand the points being made, asking questions as appropriate, and not interrupting at inappropriate times.",
            "Using mathematics to solve problems.",
            "Understanding written sentences and paragraphs in work-related documents.",
            "Using scientific rules and methods to solve problems.",
            "Talking to others to convey information effectively.",
            "Communicating effectively in writing as appropriate for the needs of the audience."
        ]
    }

    st.table(basic_skills_data)

    st.subheader("Jobs")
    st.write(
        "In the context of job analysis and design, it is useful to represent a job as a matrix of work activities (rows) "
        "and basic skills (columns):"
    )
    
    st.latex(r'''
    J_i = 
    \begin{pmatrix}
    s_{11} & s_{12} & s_{13} & s_{14} & s_{15} & s_{16} \\
    s_{21} & s_{22} & s_{23} & s_{24} & s_{25} & s_{26} \\
    s_{31} & s_{32} & s_{33} & s_{34} & s_{35} & s_{36} \\
    s_{41} & s_{42} & s_{43} & s_{44} & s_{45} & s_{46} \\
    \end{pmatrix}
    ''')
    
    st.write(
        "Each element \( x_{ij} \) of the matrix indicates the extent to which basic skill \( j \) is required for work activity \( i \):"
    )
    
    st.latex(r'''
    0 \leq s_{ij} \leq 100
    ''')

    st.write(
        "A job may not require all 10 work activities. If a job does not include a particular work activity, "
        "the corresponding row will be removed."
    )

    st.subheader("Job Evaluation and Job Complexity")
    st.write(
        "Job evaluation is a systematic process used to assess the relative worth of jobs within an organization. "
        "This assessment considers various job characteristics, such as responsibilities, required skills, and the complexity of the work activities involved. "
        "By conducting a job evaluation, organizations can establish equitable compensation structures and identify training and development needs."
    )

    st.write(
        "As an example of job evaluation, job complexity serves as a key metric in understanding the intricacies involved in different roles. "
        "Job complexity reflects the degree of difficulty associated with work activities and the range of skills necessary to perform them effectively. "
        "To quantify job complexity, we calculate the total skill requirements by summing all elements in the job matrix \( J \):"
    )

    st.latex(r'''
    \text{Job complexity} = \sum_{i=1}^{4} \sum_{j=1}^{6} s_{ij}
    ''')

    st.write(
        "This formula provides a quantitative measure of the job's complexity by considering the required skill levels across various activities, "
        "thereby offering valuable insights for effective job design and organizational planning."
    )

    st.subheader("Task Similarity")
    st.write(
        "The cosine similarity between two work activities \( WA_i \) and \( WA_j \) is defined as follows:"
    )

    st.latex(r'''
    \text{Cosine Similarity}(\text{WA}_i, \text{WA}_j) = \frac{\text{WA}_i \cdot \text{WA}_j}{\|\text{WA}_i\| \|\text{WA}_j\|}
    ''')

    st.write(
        "Where:"
    )
    
    st.markdown(
        "- \( \text{WA}_i \cdot \text{WA}_j \) represents the dot product of the skill vectors for work activities \( \text{WA}_i \) and \( \text{WA}_j \), calculated as:"
    )
    
    st.latex(r'''
    \text{WA}_i \cdot \text{WA}_j = \sum_{k=1}^{6} s_{ik} s_{jk}
    ''')
    
    st.markdown(
        "- \( \|\text{WA}_i\| \) and \( \|\text{WA}_j\| \) denote the magnitudes of the skill vectors for work activities \( \text{WA}_i \) and \( \text{WA}_j \), calculated using:"
    )
    
    st.latex(r'''
    \|\text{WA}_i\| = \sqrt{\sum_{k=1}^{6} s_{ik}^2}
    ''')

