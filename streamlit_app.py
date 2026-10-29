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

# Skill learning resources
resources = {
    "Python": "Python programming tutorials",
    "Java": "Java programming course",
    "C": "C programming tutorials
