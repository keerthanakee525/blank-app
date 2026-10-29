import streamlit as st
import re
import pymupdf

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Resume Analyzer & Skill Gap Detector")

st.write(
    "Upload your resume, discover your skills, "
    "identify skill gaps, and improve your career readiness!"
)

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

# Skill aliases
skill_aliases = {
    "Python": ["python"],
    "Java": ["java"],
    "C": ["c", "c programming", "c language"],
    "Data Structures": ["data structures", "dsa"],
    "Algorithms": ["algorithms", "algorithm"],
    "SQL": ["sql", "mysql", "postgresql"],
    "Git": ["git", "github"],
    "Problem Solving": ["problem solving"],
    "HTML": ["html"],
    "CSS": ["css"],
    "JavaScript": ["javascript", "js"],
    "React": ["react", "reactjs", "react.js"],
    "Node.js": ["node.js", "nodejs"],
    "Excel": ["excel", "microsoft excel"],
    "Power BI": ["power bi", "powerbi"],
    "Statistics": ["statistics"],
    "Data Visualization": ["data visualization"],
    "Networking": ["networking", "computer networks"],
    "Linux": ["linux"],
    "Cybersecurity": ["cybersecurity", "cyber security"],
    "Ethical Hacking": ["ethical hacking"],
    "Machine Learning": ["machine learning", "ml"],
    "Deep Learning": ["deep learning"],
    "TensorFlow": ["tensorflow"]
}

def detect_skills(text):
    detected = []

    for skill, aliases in skill_aliases.items():
        for alias in aliases:
            pattern = (
                r"(?<![a-zA-Z0-9])"
                + re.escape(alias)
                + r"(?![a-zA-Z0-9])"
            )

            if re.search(pattern, text, re.IGNORECASE):
                detected.append(skill)
                break

    return detected


def extract_pdf_text(uploaded_file):
    text = ""

    with pymupdf.open(
        stream=uploaded_file.getvalue(),
        filetype="pdf"
    ) as document:

        for page in document:
            text += page.get_text() + "\n"

    return text


st.divider()

st.subheader("👤 Student Details")

name = st.text_input("Enter Your Name")

role = st.selectbox(
    "💼 Select Your Dream Job",
    list(job_skills.keys())
)

st.divider()

st.subheader("📄 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your resume in PDF format",
    type=["pdf"]
)

st.write("OR")

manual_skills = st.text_area(
    "🛠️ Enter Your Skills Manually",
    placeholder="Example: Python, C, SQL, HTML"
)

resume_text = ""

if uploaded_file is not None:

    try:
        resume_text = extract_pdf_text(uploaded_file)

        if resume_text.strip():
            st.success("✅ Resume uploaded and read successfully!")
        else:
            st.warning(
                "No readable text found. "
                "Please use a text-based PDF resume."
            )

    except Exception as e:
        st.error("Unable to read this PDF.")
        st.write(str(e))


if st.button("🔍 Analyze My Resume"):

    combined_text = resume_text + "\n" + manual_skills

    if not combined_text.strip():
        st.warning(
            "Please upload a readable resume or enter your skills."
        )

    else:

        detected = detect_skills(combined_text)

        required = job_skills[role]

        matched = [
            skill for skill in required
            if skill in detected
        ]

        missing = [
            skill for skill in required
            if skill not in detected
        ]

        percentage = round(
            len(matched) / len(required) * 100,
            2
        )

        st.divider()

        st.success(
            f"Analysis completed for {name or 'Student'}!"
        )

        st.subheader("🧠 Automatically Detected Skills")

        if detected:
            st.write(", ".join(detected))
        else:
            st.info("No supported skills detected.")

        st.subheader("📊 Skill Match Score")

        st.metric(
            "Skill Match Percentage",
            f"{percentage}%"
        )

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
                st.success("All required skills matched!")

        st.divider()

        st.subheader("📚 Personalized Learning Roadmap")

        if missing:

            for i, skill in enumerate(missing, 1):

                st.write(f"### Step {i}: Learn {skill}")

                st.write(
                    f"📖 Study {skill} using beginner tutorials."
                )

                st.write(
                    "🎯 Practice with exercises and projects."
                )

        else:

            st.success(
                "Great! Focus on advanced projects "
                "and interview preparation."
            )

        st.divider()

        st.subheader("🚀 Career Readiness Feedback")

        if percentage >= 80:

            feedback = (
                "Excellent skill coverage! "
                "Continue building real-world projects."
            )

            st.success(feedback)

        elif percentage >= 50:

            feedback = (
                "Good progress! Focus on improving "
                "your missing skills."
            )

            st.info(feedback)

        else:

            feedback = (
                "Keep learning! Follow your personalized "
                "roadmap to improve your skills."
            )

            st.warning(feedback)

        st.divider()

        st.subheader("📥 Download Your Analysis Report")

        report = f"""
AI RESUME ANALYZER REPORT

Student Name: {name or 'Student'}

Target Job: {role}

Skill Match: {percentage}%

Detected Skills:
{', '.join(detected) if detected else 'None'}

Matched Skills:
{', '.join(matched) if matched else 'None'}

Missing Skills:
{', '.join(missing) if missing else 'None'}

LEARNING ROADMAP:
"""

        for i, skill in enumerate(missing, 1):
            report += (
                f"\n{i}. Learn {skill}"
                "\n   Practice with tutorials and projects.\n"
            )

        report += f"\nCAREER FEEDBACK:\n{feedback}\n"

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="skill_gap_report.txt",
            mime="text/plain"
        )

st.divider()

st.caption(
    "AI Resume Analyzer & Skill Gap Detector | Student Project"
)
