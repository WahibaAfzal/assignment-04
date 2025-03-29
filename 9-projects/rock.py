import streamlit as st
import random

st.title("🎮 Rock, Paper, Scissors Game! 🪨📄✂️")

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Session state to track scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0

st.write("Choose your move:")

# Buttons for user input
col1, col2, col3 = st.columns(3)
if col1.button("🪨 Rock"):
    user_choice = "rock"
elif col2.button("📄 Paper"):
    user_choice = "paper"
elif col3.button("✂️ Scissors"):
    user_choice = "scissors"
else:
    user_choice = None

if user_choice:
    computer_choice = random.choice(choices)
    st.write(f"🤖 Computer chose: **{computer_choice.capitalize()}**")

    # Determine winner
    if user_choice == computer_choice:
        st.write("😐 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        st.write("🎉 You win this round!")
        st.session_state.user_score += 1
    else:
        st.write("💀 Computer wins this round!")
        st.session_state.computer_score += 1

    # Display scores
    st.write(f"📊 **Score:** You: {st.session_state.user_score} | Computer: {st.session_state.computer_score}")

# Reset button
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.rerun()
