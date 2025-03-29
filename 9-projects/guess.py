import streamlit as st
import random

# Initialize game state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = ""

st.title("🎮 Guess the Number Game!")
st.write("Guess a number between **1 and 100**!")

# User input
guess = st.number_input("Your guess:", min_value=1, max_value=100, step=1)

if st.button("Check"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.session_state.message = "🔼 Too low! Try again."
    elif guess > st.session_state.number:
        st.session_state.message = "🔽 Too high! Try again."
    else:
        st.session_state.message = f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts! 🎊"
        st.balloons()

st.write(st.session_state.message)

if st.button("🔄 Restart"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = ""
