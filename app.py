import streamlit as st

# Streamlit Page Configuration
st.set_page_config(page_title="My Portfolio", page_icon=":briefcase:", layout="wide")

# Add a background image to the app
background_image_url = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920"
st.markdown(
    f"""
    <style>
        .main {{
            background-image: url({background_image_url});
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            min-height: 100vh;
            padding: 50px;
        }}
        .header {{
            text-align: center;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.6);  /* Dark transparent background */
            color: white;
        }}
        .section {{
            background-color: rgba(0, 0, 0, 0.7);  /* Dark transparent background for sections */
            padding: 30px;
            border-radius: 10px;
            color: white;
            margin-top: 30px;
        }}
        .sidebar {{
            background-color: rgba(0, 0, 0, 0.5);  /* Dark transparent background for sidebar */
        }}
        .social-icons {{
            font-size: 30px;
            margin: 10px;
            color: white;
            transition: color 0.3s;
        }}
        .social-icons:hover {{
            color: #00acee;  /* Example: color change on hover (Twitter blue) */
        }}
    </style>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    """, unsafe_allow_html=True
)

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "My Projects", "Profiles"])

# Page: Home
if page == "Home":
    st.markdown("<div class='header'><h1>Welcome to My Portfolio!</h1></div>", unsafe_allow_html=True)
    st.write("""
    Hi, I'm **Sijon Chisty Saon**, a passionate learner and developer with a strong background in Computer Science & Engineering. 
    I am currently pursuing my B.Sc. in CSE from **Bangladesh University of Engineering & Technology**.
    I enjoy building projects, learning new technologies, and collaborating with others to create impactful solutions.
    
    ### About Me
    - **Name**: Sijon Chisty Saon
    - **Location**: Dhaka, Bangladesh
    - **Profession**: Student (B.Sc. in CSE, Level-2, Term-2)
    - **Interests**: Web Development, Data Science, Machine Learning, Open Source
    
    Feel free to explore the other sections to see my projects and profiles.
    """)

# Page: My Projects
elif page == "My Projects":
    st.markdown("<div class='header'><h1>My Projects</h1></div>", unsafe_allow_html=True)
    st.write("Here are some of the projects I've worked on:")

    # Example projects
    projects = [
        {"title": "Jobster", "description": "Connecting employers and employees to make the job finding, interview scheduling, appointment process easier.", "link": "https://github.com/Saon110/Jobster"},
        {"title": "Travel Buddy", "description": "AI companion for travelers, making their trips easier.", "link": "https://github.com/Saon110/Travel-Buddy"},
        {"title": "Muslim's Day", "description": "Daily Islamic Schedule.", "link": "https://github.com/Saon110/Muslim-s-Day"},
    ]

    for project in projects:
        st.markdown(f"""
        - **[{project['title']}]({project['link']})**: {project['description']}
        """)

# Page: Profiles
elif page == "Profiles":
    st.markdown("<div class='header'><h1>My Profiles</h1></div>", unsafe_allow_html=True)
    st.write("""
    You can connect with me on the following platforms:
    """)

    # Example profiles with icons
    profiles = {
        "LinkedIn": "https://www.linkedin.com/in/sijon-chisty-saon-745095252/",
        "GitHub": "https://github.com/Saon110",
        "Twitter": "https://x.com/Saon_chishty",
        "Facebook": "https://www.facebook.com/sijonchisty",
        "Portfolio": "https://sijon-chisty-saon.streamlit.app/",
    }

    for platform, link in profiles.items():
        # Adding the Font Awesome icons next to the platform name
        if platform == "LinkedIn":
            icon = '<i class="fab fa-linkedin social-icons"></i>'
        elif platform == "GitHub":
            icon = '<i class="fab fa-github social-icons"></i>'
        elif platform == "Twitter":
            icon = '<i class="fab fa-twitter social-icons"></i>'
        elif platform == "Facebook":
            icon = '<i class="fab fa-facebook social-icons"></i>'
        elif platform == "Portfolio":
            icon = '<i class="fas fa-laptop-code social-icons"></i>'  # Portfolio icon

        st.markdown(f'<a href="{link}" target="_blank">{icon}</a>', unsafe_allow_html=True)

    st.write("""
    Feel free to reach out to me for collaboration, questions, or just a chat!
    """)
