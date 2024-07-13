import random
import streamlit as st
import time
random.seed(time.time())

questions = {
    "what is the capital of france ?" : {"choices" : ["Paris","london","berlin"],"answer": "paris"},
    "What is 2 + 2 ?": {"choices" : ["3","22","4"],"answer": "4"},
    "What is the hottest planet in our solar system?" : {"choices" : ["mars","earth","venus"],"answer": "venus"},
    "What is 8 + 9 ?": {"choices" : ["8","89","17"],"answer": "17"},
    "who is the best footballer ever" : {"choices" : ["Mbappe","Messi","shareef"],"answer":"Shareef"},
    "What goes up and never goes down " : {"choices" : ["age","airballoon","balloon"], "answer" : "age"},
    "What is 30 + 23 " : {"choices" : ["53","40","98"], "answer" : "53"},
    "Who is the fastest person ever " : {"choices" : ["Usain Bolt","Noah Lyles","Kylian Mbappe"], "answer" : "Usain Bolt"},
    "Who is the best racer " : {"choices" : ["Usain Bolt","luis Hamilton","trossard"], "answer" : "Luis Hamilton"},
    "What 10 * 5 " : {"choices" : ["50","150","89"], "answer" : "50"},
}

def initialize_quiz():
    items = list(questions.items())
    random.shuffle(items)
    st.session_state.quiz_questions = items
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.quiz_completed = False
    st.session_state.answer_submitted = False  # Track if the answer has been submitted

if 'quiz_questions' not in st.session_state:
    initialize_quiz()

def display_question():
    question, data = st.session_state.quiz_questions[st.session_state.current_question_index]
    st.write(question)
    choices = ["Select your answer"] + data['choices']
    user_answer = st.radio("Choose one:", choices, index=0, key=f"choice{st.session_state.current_question_index}")
    return user_answer

def handle_answer(user_answer):
    if not st.session_state.answer_submitted and user_answer != "Select your answer":
        st.session_state.answer_submitted = True  # Mark the answer as submitted
        question, data = st.session_state.quiz_questions[st.session_state.current_question_index]
        if user_answer == data['answer']:
            st.session_state.score += 1
            st.success('Correct!')
        else:
            st.error(f'Wrong! The correct answer was {data["answer"]}.')
    elif st.session_state.answer_submitted:
        # Advance to the next question or finish quiz
        if st.session_state.current_question_index < len(st.session_state.quiz_questions) - 1:
            st.session_state.current_question_index += 1
            st.session_state.answer_submitted = False  # Reset for the next question
            st.experimental_rerun()
        else:
            st.session_state.quiz_completed = True
            st.write(f"Quiz completed! Your final score is {st.session_state.score}/{len(st.session_state.quiz_questions)}.")

def reset_quiz():
    if st.button('Restart Quiz'):
        initialize_quiz()
        st.experimental_rerun()

user_answer = display_question()

button_label = "Next Question" if st.session_state.answer_submitted else "Submit Answer"
if st.button(button_label, key='submit'):
    handle_answer(user_answer)

if st.session_state.quiz_completed:
    reset_quiz()
