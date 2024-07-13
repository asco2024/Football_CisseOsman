import random
import streamlit as st
import time
random.seed(time.time())

questions = {
    "Who scored the first goal for aberdeen in holland Rood Wit tournement?" : {"choices" : ["Carter","Cisse","Huddson"],"answer": "Cisse"},
    "Who won the award for the best goal of the season?" : {"choices" : ["Freddie","Nile","Jack"],"answer": "Jack"},
    "Who was the captain for the Rood Wit tournement" : {"choices" : ["Alex","Carter","Huddson"],"answer": "Huddson"},
    "what team is going to win the euro 2024" : {"choices" : ["England","Spain"],"answer": "Spain"},
    "What position did we finish when we played the Rood Wit tournement" : {"choices" : ["5th","9th","11th"],"answer": "Spain"},
    "How many European cups has aberdeen won" : {"choices" : ["4","2","1"],"answer": "2"},
    "Which of the following coaches has gone to manage 5 teams" : {"choices" : ["Alex ferguson","Pep Guardiola","Gareth Southgate"],"answer": "Alex ferguson"},
    "who is the youngest player in euro 2024" : {"choices" : ["mbappe","Nico Williams","Yamal"],"answer": "Alex ferguson"},
    "How many Scottish league titles has Aberdeen FC won?" : {"choices" : ["5","4 ","6"],"answer": "4"},
    "When did Aberdeen fc start playing football" : {"choices" : ["1903","1826","1951"],"answer": "Alex ferguson"},
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
