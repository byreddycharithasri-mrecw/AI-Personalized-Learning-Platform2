import streamlit as st
import json
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Personalized Learning Platform",
    page_icon="🎓",
    layout="wide"
)

# ============================================================
# SESSION STATE
# ============================================================

if "progress" not in st.session_state:
    st.session_state.progress = {}

if "study_plan" not in st.session_state:
    st.session_state.study_plan = ""

if "quiz" not in st.session_state:
    st.session_state.quiz = []

if "score" not in st.session_state:
    st.session_state.score = None

if "documents" not in st.session_state:
    st.session_state.documents = {}


# ============================================================
# STUDY PLAN FUNCTION
# ============================================================

def create_study_plan(name, subject, level, goal, hours, days):

    plan = f"""
# 📚 Personalized Study Plan

## Student Details

**Name:** {name}

**Subject:** {subject}

**Level:** {level}

**Goal:** {goal}

**Study Time:** {hours} hours per day

**Duration:** {days} days

---

## 🎯 Learning Objectives

1. Understand the fundamentals of {subject}.
2. Learn important concepts step by step.
3. Practice problems regularly.
4. Review mistakes.
5. Complete a final assessment.

---

## 📅 Daily Plan

### Days 1 - 5
Learn the basic concepts of {subject}.

### Days 6 - 10
Practice simple problems and examples.

### Days 11 - 15
Learn intermediate concepts.

### Days 16 - 20
Solve practical problems.

### Days 21 - 25
Work on mini projects and applications.

### Days 26 - 30
Revision and practice tests.

---

## ⏰ Daily Routine

- 30 minutes: Learn concepts
- 45 minutes: Practice
- 30 minutes: Solve problems
- 15 minutes: Revision

---

## 💡 Tips

- Practice every day.
- Make short notes.
- Review mistakes.
- Ask questions when you are confused.
- Revise regularly.
"""

    return plan


# ============================================================
# TOPIC EXPLANATION
# ============================================================

def explain_topic(topic, level):

    return f"""
# 🧑‍🏫 {topic}

## Simple Explanation

{topic} is a concept that can be learned by understanding its
basic principles and then practicing with examples.

## Your Level

**{level}**

## How to Learn

1. Start with the basic definition.
2. Understand the important concepts.
3. Look at simple examples.
4. Practice questions.
5. Review your mistakes.

## Example

Try to explain **{topic}** in your own words.

## Important Points

- Understand rather than only memorize.
- Practice regularly.
- Review difficult concepts.
- Apply the concept to practical examples.

## 📝 Practice Question

What is **{topic}** and where can it be used?
"""


# ============================================================
# QUIZ GENERATOR
# ============================================================

def create_quiz(topic):

    return [
        {
            "question": f"What is an important first step when learning {topic}?",
            "options": [
                "Understand the basics",
                "Skip the basics",
                "Avoid practice",
                "Stop studying"
            ],
            "answer": "Understand the basics"
        },
        {
            "question": f"What is useful for improving your knowledge of {topic}?",
            "options": [
                "Regular practice",
                "Never revising",
                "Avoiding examples",
                "Ignoring mistakes"
            ],
            "answer": "Regular practice"
        },
        {
            "question": f"What should you do when you make a mistake in {topic}?",
            "options": [
                "Ignore it",
                "Review the mistake",
                "Stop learning",
                "Delete your notes"
            ],
            "answer": "Review the mistake"
        },
        {
            "question": f"Which method is best for learning {topic}?",
            "options": [
                "Only memorizing",
                "Understanding and practicing",
                "Never asking questions",
                "Skipping examples"
            ],
            "answer": "Understanding and practicing"
        },
        {
            "question": f"How can you improve your {topic} knowledge?",
            "options": [
                "Practice regularly",
                "Never revise",
                "Avoid questions",
                "Stop practicing"
            ],
            "answer": "Practice regularly"
        }
    ]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎓 AI Learning Platform")

    st.divider()

    page = st.radio(
        "Select Page",
        [
            "🏠 Dashboard",
            "📚 Study Plan",
            "🧑‍🏫 AI Tutor",
            "📝 Quiz",
            "📄 Documents",
            "📊 Progress"
        ]
    )

    st.divider()

    st.subheader("Student Profile")

    student_name = st.text_input(
        "Name",
        "Student"
    )

    student_level = st.selectbox(
        "Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    subject = st.text_input(
        "Subject",
        "Python Programming"
    )


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.title(
        "🎓 AI Personalized Learning Platform"
    )

    st.write(
        "Learn, practice, take quizzes and track your progress."
    )

    st.divider()

    completed = 0

    for value in st.session_state.progress.values():

        if value:
            completed += 1

    total = len(
        st.session_state.progress
    )

    if total > 0:
        percentage = int(
            completed / total * 100
        )
    else:
        percentage = 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Level",
            student_level
        )

    with col2:
        st.metric(
            "Topics",
            total
        )

    with col3:
        st.metric(
            "Completed",
            completed
        )

    with col4:
        st.metric(
            "Progress",
            f"{percentage}%"
        )

    st.divider()

    st.subheader(
        "🚀 Learning Features"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "📚 Study Plan\n\n"
            "Create a personalized study schedule."
        )

    with col2:
        st.info(
            "🧑‍🏫 AI Tutor\n\n"
            "Get simple explanations for topics."
        )

    with col3:
        st.info(
            "📝 Quiz\n\n"
            "Test your knowledge."
        )


# ============================================================
# STUDY PLAN
# ============================================================

elif page == "📚 Study Plan":

    st.title(
        "📚 Personalized Study Plan"
    )

    goal = st.text_area(
        "What is your learning goal?",
        placeholder="Example: Learn Python in 30 days"
    )

    hours = st.slider(
        "Study hours per day",
        1,
        8,
        2
    )

    days = st.slider(
        "Number of days",
        7,
        90,
        30
    )

    if st.button(
        "✨ Create Study Plan",
        use_container_width=True
    ):

        if goal.strip() == "":

            st.error(
                "Please enter your learning goal."
            )

        else:

            st.session_state.study_plan = create_study_plan(
                student_name,
                subject,
                student_level,
                goal,
                hours,
                days
            )

            st.success(
                "Study plan created successfully!"
            )

    if st.session_state.study_plan:

        st.divider()

        st.markdown(
            st.session_state.study_plan
        )


# ============================================================
# AI TUTOR
# ============================================================

elif page == "🧑‍🏫 AI Tutor":

    st.title(
        "🧑‍🏫 AI Tutor"
    )

    topic = st.text_input(
        "Enter a topic",
        placeholder="Example: Python loops"
    )

    if st.button(
        "🧠 Explain Topic",
        use_container_width=True
    ):

        if topic.strip() == "":

            st.error(
                "Please enter a topic."
            )

        else:

            explanation = explain_topic(
                topic,
                student_level
            )

            st.markdown(
                explanation
            )

            if topic not in st.session_state.progress:

                st.session_state.progress[
                    topic
                ] = False

    st.divider()

    st.subheader(
        "Mark Topic as Completed"
    )

    topics = list(
        st.session_state.progress.keys()
    )

    if topics:

        selected = st.selectbox(
            "Select Topic",
            topics
        )

        if st.button(
            "✅ Mark Completed"
        ):

            st.session_state.progress[
                selected
            ] = True

            st.success(
                f"{selected} completed!"
            )

    else:

        st.info(
            "Study a topic first."
        )


# ============================================================
# QUIZ
# ============================================================

elif page == "📝 Quiz":

    st.title(
        "📝 Knowledge Quiz"
    )

    topic = st.text_input(
        "Quiz Topic",
        subject
    )

    number = st.slider(
        "Number of Questions",
        2,
        5,
        5
    )

    if st.button(
        "🎯 Generate Quiz",
        use_container_width=True
    ):

        st.session_state.quiz = create_quiz(
            topic
        )[:number]

        st.session_state.score = None

        st.success(
            "Quiz generated!"
        )

    if st.session_state.quiz:

        answers = []

        st.divider()

        for i, question in enumerate(
            st.session_state.quiz
        ):

            st.subheader(
                f"Question {i + 1}"
            )

            st.write(
                question["question"]
            )

            answer = st.radio(
                "Select answer",
                question["options"],
                key=f"question_{i}"
            )

            answers.append(
                answer
            )

        if st.button(
            "📊 Submit Quiz",
            use_container_width=True
        ):

            score = 0

            for i, question in enumerate(
                st.session_state.quiz
            ):

                if answers[i] == question["answer"]:

                    score += 1

            st.session_state.score = score

    if st.session_state.score is not None:

        total_questions = len(
            st.session_state.quiz
        )

        score = st.session_state.score

        percentage = int(
            score / total_questions * 100
        )

        st.divider()

        if percentage >= 80:

            st.success(
                f"🎉 Excellent! "
                f"{score}/{total_questions} "
                f"({percentage}%)"
            )

        elif percentage >= 60:

            st.info(
                f"👍 Good! "
                f"{score}/{total_questions} "
                f"({percentage}%)"
            )

        else:

            st.warning(
                f"📖 Keep practicing! "
                f"{score}/{total_questions} "
                f"({percentage}%)"
            )


# ============================================================
# DOCUMENTS
# ============================================================

elif page == "📄 Documents":

    st.title(
        "📄 My Documents"
    )

    st.write(
        "Upload TXT files and keep them inside your learning platform."
    )

    uploaded_file = st.file_uploader(
        "Upload a TXT file",
        type=["txt"]
    )

    if uploaded_file:

        if st.button(
            "📥 Save Document"
        ):

            content = uploaded_file.read().decode(
                "utf-8",
                errors="ignore"
            )

            st.session_state.documents[
                uploaded_file.name
            ] = content

            st.success(
                f"{uploaded_file.name} saved successfully!"
            )

    if st.session_state.documents:

        st.divider()

        st.subheader(
            "Saved Documents"
        )

        for filename, content in (
            st.session_state.documents.items()
        ):

            with st.expander(
                f"📄 {filename}"
            ):

                st.write(
                    content
                )

    else:

        st.info(
            "No documents uploaded yet."
        )


# ============================================================
# PROGRESS
# ============================================================

elif page == "📊 Progress":

    st.title(
        "📊 Learning Progress"
    )

    if not st.session_state.progress:

        st.info(
            "No topics added yet."
        )

    else:

        completed = 0

        total = len(
            st.session_state.progress
        )

        for topic, status in (
            st.session_state.progress.items()
        ):

            if status:

                completed += 1

                st.success(
                    f"✅ {topic} - Completed"
                )

            else:

                st.info(
                    f"📖 {topic} - In Progress"
                )

        if total > 0:

            percentage = completed / total

        else:

            percentage = 0

        st.divider()

        st.subheader(
            "Overall Progress"
        )

        st.progress(
            percentage
        )

        st.write(
            f"{completed} of {total} topics completed"
        )

        st.write(
            f"Progress: {percentage * 100:.0f}%"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎓 AI Personalized Learning Platform | Python + Streamlit"
)