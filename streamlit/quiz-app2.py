# Upgrade your Streamlit Quiz App with:
# ✅ A balloon celebration animation when the quiz ends
# ✅ A bar chart of results (correct vs. incorrect)
# ✅ A downloadable CSV file of the user’s responses

import streamlit as st
import pandas as pd

# --- Quiz Data (List of Dicts) ---
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

# --- Initialize Session State ---
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "selected_answers" not in st.session_state:
    st.session_state.selected_answers = []
if "show_result" not in st.session_state:
    st.session_state.show_result = False
# if "show_anim" not in st.session_state:
#     st.session_state.show_anim = True

# --- Functions ---
def next_question(selected_option):
    st.session_state.selected_answers.append(selected_option)
    st.session_state.current_q += 1
    if st.session_state.current_q >= len(quiz_data):
        st.session_state.show_result = True

def restart_quiz():
    st.session_state.current_q = 0
    st.session_state.selected_answers = []
    st.session_state.show_result = False

# --- App Title ---
st.title("🧠 Simple Quiz App (Python + Streamlit)")
st.caption("Demonstration project using built-in data structures (list + dict)")

# --- Progress ---
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

    st.button("Next ➡️", on_click=next_question, args=(selected_option,))

else:
    # --- Result Calculation ---
    score = 0
    results = []
    for i, q in enumerate(quiz_data):
        user_ans = st.session_state.selected_answers[i]
        correct = q["answer"]
        is_correct = user_ans == correct
        if is_correct:
            score += 1
        results.append({
            "Question": q["question"],
            "Your Answer": user_ans,
            "Correct Answer": correct,
            "Result": "✅ Correct" if is_correct else "❌ Incorrect"
        })

    # --- Celebration ---
    st.snow()
    # st.balloons()
    # if st.session_state.show_anim:
    #   st.balloons()
    #   st.session_state.show_anim = False

    # --- Display Results ---
    st.success(f"🎉 Quiz Completed! Your Score: **{score}/{total_questions}**")

    df_results = pd.DataFrame(results)
    st.write("### 📊 Detailed Results")
    st.dataframe(df_results, use_container_width=True)

    # --- Result Chart ---
    st.write("### 📈 Performance Chart")
    chart_data = pd.DataFrame({
        "Type": ["Correct", "Incorrect"],
        "Count": [score, total_questions - score]
    })
    st.bar_chart(chart_data.set_index("Type"))

    # --- Download as CSV ---
    csv_data = df_results.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Results as CSV",
        data=csv_data,
        file_name="quiz_results.csv",
        mime="text/csv"
    )

    # --- Restart Button ---
    st.button("🔄 Restart Quiz", on_click=restart_quiz)
