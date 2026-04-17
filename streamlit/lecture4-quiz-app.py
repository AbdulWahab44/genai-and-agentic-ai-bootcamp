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

# ----------- Initialize session state ---------------
if "current_q" not in st.session_state:
  st.session_state.current_q = 0
if "selected_answers" not in st.session_state:
  st.session_state.selected_answers = []
if "show_result" not in st.session_state:
  st.session_state.show_result = False

def next_question(selected_option):
  st.session_state.selected_answers.append(selected_option)
  st.session_state.current_q += 1
  if st.session_state.current_q >= len(quiz_data):
    st.session_state.show_result = True

def restart_quiz():
  st.session_state.current_q = 0
  st.session_state.selected_answers = []
  st.session_state.show_result = False


# --- Header ----
st.title("Simple Quiz App")
st.caption("This is a teaching quiz app.")

# ------------ Progress Bar --------------
total_questions = len(quiz_data)
current_q = st.session_state.current_q
progress = current_q / total_questions
st.progress(progress)
st.write(f"**Question: {current_q + 1} of {total_questions}**")


if not st.session_state.show_result:
  current_q = st.session_state.current_q
  q = quiz_data[current_q]
  st.subheader(q["question"])
  selected_option = st.radio(
    "Choose an answer:",
    q["options"],
    key=f"q_{current_q}"
  )

  st.button(
    "Next",
    on_click=next_question,
    args = (selected_option,)
  )
else:
  st.write("End of quiz")
  st.button("Restart Quiz", on_click=restart_quiz)








# it has some limitations
# if st.button("Next"):
#   st.session_state.current_q += 1