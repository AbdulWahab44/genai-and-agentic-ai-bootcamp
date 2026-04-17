import streamlit as st

# --- Quiz Data (list of dicts) ---
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which language is primarily used for data science?",
        "options": ["Python", "C++", "HTML", "Java"],
        "answer": "Python"
    },
    {
        "question": "Which of the following is a Python web framework?",
        "options": ["React", "Flask", "Laravel", "Spring"],
        "answer": "Flask"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "HighText Machine Language",
            "HyperTabular Markup Language",
            "None of these"
        ],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which of the following is used to style web pages?",
        "options": ["HTML", "CSS", "Python", "Java"],
        "answer": "CSS"
    }
]

# --- Initialize session state ---
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "selected_answers" not in st.session_state:
    st.session_state.selected_answers = []
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# --- Function to move to next question ---
def next_question(selected_option):
    st.session_state.selected_answers.append(selected_option)
    st.session_state.current_q += 1
    if st.session_state.current_q >= len(quiz_data):
        st.session_state.show_result = True

# --- Function to restart quiz ---
def restart_quiz():
    st.session_state.current_q = 0
    st.session_state.selected_answers = []
    st.session_state.show_result = False

# --- Title ---
st.title("🧠 Simple Quiz App (Python + Streamlit)")
st.caption("Demonstration project using built-in data structures (list + dict)")

# --- Progress Bar ---
total_questions = len(quiz_data)
current_q = st.session_state.current_q
progress = current_q / total_questions
st.progress(progress)

st.write(f"**Question {min(current_q + 1, total_questions)} of {total_questions}**")

# --- Display Questions or Results ---
if not st.session_state.show_result:
    q = quiz_data[current_q]
    st.subheader(q["question"])
    selected_option = st.radio(
        "Choose an answer:",
        q["options"],
        key=f"q_{current_q}"
    )

    st.button(
        "Next ➡️",
        on_click=next_question,
        args=(selected_option,)
    )

else:
    # --- Calculate Result ---
    score = 0
    for i, q in enumerate(quiz_data):
        if i < len(st.session_state.selected_answers) and st.session_state.selected_answers[i] == q["answer"]:
            score += 1

    st.success(f"🎉 Quiz Completed! Your Score: {score}/{total_questions}")

    st.write("### Review:")
    for i, q in enumerate(quiz_data):
        user_ans = st.session_state.selected_answers[i]
        correct = q["answer"]
        if user_ans == correct:
            st.markdown(f"✅ **Q{i+1}. {q['question']}** — Your answer: **{user_ans}**") # tick icon text
        else:
            st.markdown(f"❌ **Q{i+1}. {q['question']}** — Your answer: **{user_ans}**, Correct: **{correct}**") # cross icon text

    st.button("🔄 Restart Quiz", on_click=restart_quiz)
