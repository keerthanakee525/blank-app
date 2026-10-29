import streamlit as st
import re

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Resume Analyzer & Skill Gap Detector")
st.write("Analyze your skills, find missing skills, and improve your career readiness!")

# Job roles and required skills
job_skills = {
    "Software Developer": [
        "Python", "Java", "C", "Data Structures",
        "Algorithms", "SQL", "Git", "Problem Solving"
    ],
    "Web Developer": [
        "HTML", "CSS", "JavaScript", "React",
        "Node.js", "SQL", "Git"
    ],
    "Data Analyst": [
        "Python", "SQL", "Excel", "Power BI",
        "Statistics", "Data Visualization"
    ],
    "Cybersecurity Analyst": [
        "Python", "Networking", "Linux",
        "Cybersecurity", "Ethical Hacking", "SQL"
    ],
    "AI/ML Engineer": [
        "Python", "Machine Learning", "Deep Learning",
        "TensorFlow", "Data Structures", "Statistics"
    ]
}

# Learning resources
resources = {
    "Python": "Learn Python programming",
    "Java": "Learn Java programming",
    "C": "Learn C programming",
    "Data Structures": "Study Data Structures",
    "Algorithms": "Practice Algorithms",
    "SQL": "Learn SQL databases",
    "Git": "Learn Git and GitHub",
    "HTML": "Learn HTML",
    "CSS": "Learn CSS",
    "JavaScript": "Learn JavaScript",
    "React": "Learn React.js",
    "Node.js": "Learn Node.js",
    "Machine Learning": "Learn Machine Learning",
    "Deep Learning": "Learn Deep Learning",
    "TensorFlow": "Learn TensorFlow",
    "Networking": "Study Computer Networks",
    "Linux": "Learn Linux commands",
    "Cybersecurity": "Learn Cybersecurity fundamentals",
    "Ethical Hacking": "Learn Ethical Hacking",
    "Excel": "Learn Advanced Excel",
    "Power BI": "Learn Power BI",
    "Statistics": "Study Statistics",
    "Data Visualization": "Learn Data Visualization",
    "Problem Solving": "Practice coding problems"
}

st.divider()

# Student details
name = st.text_input("👤 Enter Your Name")

role = st.selectbox(
    "💼 Select Your Dream Job",
    list(job_skills.keys())
)

skills_input = st.text_area(
    "🛠️ Enter Your Current Skills",
    placeholder="Example: Python, C, SQL, HTML"
)

# Analyze button
if st.button("🔍 Analyze My Skills"):

    if not skills_input.strip():
        st.warning("Please enter your skills first.")

    else:
        required = job_skills[role]

        entered = [
            skill.strip().lower()
            for skill in re.split(r"[,\n]+", skills_input)
            if skill.strip()
        ]

        matched = [
            skill for skill in required
            if skill.lower() in entered
        ]

        missing = [
            skill for skill in required
            if skill.lower() not in entered
        ]

        percentage = round(
            (len(matched) / len(required)) * 100, 2
        )

        st.success(
            f"Analysis completed for {name or 'Student'}!"
        )

        st.subheader("📊 Your Skill Match Score")
        st.metric("Skill Match", f"{percentage}%")
        st.progress(percentage / 100)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Skills")
            if matched:
                for skill in matched:
                    st.success(skill)
            else:
                st.info("No matching skills found.")

        with col2:
            st.subheader("❌ Missing Skills")
            if missing:
                for skill in missing:
                    st.error(skill)
            else:
                st.success("You have all the listed skills!")

        st.divider()

        st.subheader("📚 Personalized Learning Roadmap")

        if missing:
            for i, skill in enumerate(missing, start=1):
                st.write(f"**Step {i}: Learn {skill}**")
                st.write(
                    f"📖 Resource: {resources.get(skill, 'Beginner tutorials')}"
                )
                st.write("🎯 Practice with a small project.")
        else:
            st.success(
                "Excellent! Focus on advanced projects and interviews."
            )

        st.divider()

        st.subheader("🚀 Career Readiness Feedback")

        if percentage >= 80:
            st.success(
                "Excellent! You have a strong foundation for this role."
            )
        elif percentage >= 50:
            st.info(
                "Good progress! Improve your missing skills."
            )
        else:
            st.warning(
                "Keep learning! Follow your roadmap to improve."
            )

st.divider()
st.caption("Developed as a Student Skill Gap Detection Project")
st.divider()
st.subheader("📄 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")
    st.write("File name:", uploaded_file.name)
