# claude
# issue: restart button
# Fully featured version of Quiz App.
# ✅ Randomized question order
# ✅ Shuffled answer options
# ✅ Countdown timer per question

import streamlit as st
import pandas as pd
import random
import time

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


# --- Configuration ---
TIME_PER_QUESTION = 10  # seconds per question

# --- Initialize Session State ---
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "selected_answers" not in st.session_state:
    st.session_state.selected_answers = []
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "shuffled_quiz" not in st.session_state:
    # Randomize question order
    st.session_state.shuffled_quiz = random.sample(quiz_data, len(quiz_data))
if "shuffled_options" not in st.session_state:
    # Shuffle options for each question
    st.session_state.shuffled_options = []
    for q in st.session_state.shuffled_quiz:
        shuffled = q["options"].copy()
        random.shuffle(shuffled)
        st.session_state.shuffled_options.append(shuffled)
if "timer_start" not in st.session_state:
    st.session_state.timer_start = time.time()
if "time_expired" not in st.session_state:
    st.session_state.time_expired = False

# --- Functions ---
def next_question(selected_option):
    st.session_state.selected_answers.append(selected_option)
    st.session_state.current_q += 1
    st.session_state.timer_start = time.time()
    st.session_state.time_expired = False
    
    if st.session_state.current_q >= len(st.session_state.shuffled_quiz):
        st.session_state.show_result = True

def handle_timeout():
    st.session_state.selected_answers.append(None)  # No answer selected
    st.session_state.current_q += 1
    st.session_state.timer_start = time.time()
    st.session_state.time_expired = False
    
    if st.session_state.current_q >= len(st.session_state.shuffled_quiz):
        st.session_state.show_result = True

def restart_quiz():
    st.session_state.current_q = 0
    st.session_state.selected_answers = []
    st.session_state.show_result = False
    st.session_state.shuffled_quiz = random.sample(quiz_data, len(quiz_data))
    st.session_state.shuffled_options = []
    for q in st.session_state.shuffled_quiz:
        shuffled = q["options"].copy()
        random.shuffle(shuffled)
        st.session_state.shuffled_options.append(shuffled)
    st.session_state.timer_start = time.time()
    st.session_state.time_expired = False

# --- App Title ---
st.title("🧠 Simple Quiz App (Python + Streamlit)")
st.caption("Demonstration project with randomized questions, shuffled options, and timer")

# --- Progress ---
total_questions = len(st.session_state.shuffled_quiz)
current_q = st.session_state.current_q
progress = current_q / total_questions
st.progress(progress)
st.write(f"**Question {min(current_q + 1, total_questions)} of {total_questions}**")

# --- Display Questions or Results ---
if not st.session_state.show_result:
    q = st.session_state.shuffled_quiz[current_q]
    shuffled_opts = st.session_state.shuffled_options[current_q]
    
    # --- Timer ---
    elapsed = time.time() - st.session_state.timer_start
    remaining = max(0, TIME_PER_QUESTION - int(elapsed))
    
    # Timer display with color coding
    timer_placeholder = st.empty()
    if remaining > 5:
        timer_placeholder.success(f"⏱️ Time Remaining: **{remaining}** seconds")
    elif remaining > 3:
        timer_placeholder.warning(f"⏱️ Time Remaining: **{remaining}** seconds")
    else:
        timer_placeholder.error(f"⏱️ Time Remaining: **{remaining}** seconds")
    
    # Check if time expired
    if remaining == 0 and not st.session_state.time_expired:
        st.session_state.time_expired = True
        st.error("⏰ Time's up! Moving to next question...")
        time.sleep(1)
        handle_timeout()
        st.rerun()
    
    st.subheader(q["question"])
    
    selected_option = st.radio(
        "Choose an answer:",
        shuffled_opts,
        key=f"q_{current_q}"
    )
    
    st.button("Next ➡️", on_click=next_question, args=(selected_option,))
    
    # Auto-refresh to update timer
    if remaining > 0:
        time.sleep(1)
        st.rerun()

else:
    # --- Result Calculation ---
    score = 0
    results = []
    for i, q in enumerate(st.session_state.shuffled_quiz):
        user_ans = st.session_state.selected_answers[i]
        correct = q["answer"]
        
        if user_ans is None:
            is_correct = False
            user_ans_display = "⏰ Time Expired"
        else:
            is_correct = user_ans == correct
            user_ans_display = user_ans
            
        if is_correct:
            score += 1
            
        results.append({
            "Question": q["question"],
            "Your Answer": user_ans_display,
            "Correct Answer": correct,
            "Result": "✅ Correct" if is_correct else "❌ Incorrect"
        })
    
    # --- Celebration ---
    st.snow()
    
    # --- Display Results ---
    percentage = (score / total_questions) * 100
    st.success(f"🎉 Quiz Completed! Your Score: **{score}/{total_questions}** ({percentage:.1f}%)")
    
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