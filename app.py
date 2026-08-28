import streamlit as st
import random

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "choices": ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
        "answer": "Blue Whale"
    },
    {
        "question": "How many continents are there on Earth?",
        "choices": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "choices": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    }
]

st.set_page_config(page_title="Quiz Game", page_icon="🎮")

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False

st.title("🎮 Quiz Game")

# Show questions
if st.session_state.current < len(st.session_state.questions):

    q = st.session_state.questions[st.session_state.current]

    st.subheader(f"Question {st.session_state.current + 1}")
    st.write(q["question"])

    answer = st.radio(
        "Choose your answer:",
        q["choices"],
        key=f"q{st.session_state.current}"
    )

    if not st.session_state.answered:
        if st.button("Submit Answer"):
            st.session_state.answered = True

            if answer == q["answer"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! Correct answer: {q['answer']}")

    if st.session_state.answered:
        if st.button("Next Question"):
            st.session_state.current += 1
            st.session_state.answered = False
            st.rerun()

    st.write(f"**Score:** {st.session_state.score}")

# Final score
else:
    total = len(st.session_state.questions)
    percentage = st.session_state.score / total * 100

    st.balloons()
    st.header("🎉 Quiz Completed!")
    st.write(f"### Score: {st.session_state.score}/{total}")
    st.write(f"### Percentage: {percentage:.1f}%")

    if percentage == 100:
        st.success("Perfect score! You're a genius! 🎉")
    elif percentage >= 70:
        st.success("Great job! You know a lot! 👏")
    elif percentage >= 40:
        st.info("Not bad, but there's room for improvement. 👍")
    else:
        st.warning("Keep learning and try again! 💪")

    if st.button("Play Again"):
        st.session_state.questions = random.sample(QUESTIONS, len(QUESTIONS))
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()
