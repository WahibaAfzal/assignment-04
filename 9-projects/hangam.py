import streamlit as st
import random

# Word list with hints
words_with_hints = {
    "apple": "🍏 A fruit that keeps doctors away.",
    "python": "🐍 A popular programming language.",
    "laptop": "💻 A portable computer.",
    "elephant": "🐘 A large animal with a trunk.",
    "streamlit": "⚡ A Python library for web apps.",
}

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word, st.session_state.hint = random.choice(list(words_with_hints.items()))
    st.session_state.guessed_word = ["_"] * len(st.session_state.word)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = set()

st.title("🎭 Emoji Hangman Game!")
st.subheader("Guess the word before you run out of hearts ❤️!")

# Show hint
st.info(f"💡 Hint: {st.session_state.hint}")

# Show word progress
st.write("**Word:** " + " ".join(st.session_state.guessed_word))

# Show lives
st.write("❤️ " * st.session_state.attempts + f"({st.session_state.attempts} attempts left)")

# Letter buttons
alphabet = "abcdefghijklmnopqrstuvwxyz"
cols = st.columns(9)  # Display buttons in multiple columns
for i, letter in enumerate(alphabet):
    if cols[i % 9].button(letter.upper(), key=letter, disabled=letter in st.session_state.guessed_letters):
        st.session_state.guessed_letters.add(letter)
        if letter in st.session_state.word:
            for i, char in enumerate(st.session_state.word):
                if char == letter:
                    st.session_state.guessed_word[i] = letter
        else:
            st.session_state.attempts -= 1

# Check for game over or win
if "_" not in st.session_state.guessed_word:
    st.success(f"🏆 You guessed the word: {st.session_state.word.upper()} 🎊")
    st.balloons()
    if st.button("🔄 Play Again"):
        st.session_state.clear()
        st.rerun()

elif st.session_state.attempts == 0:
    st.error(f"💀 Game Over! The word was: {st.session_state.word.upper()}")
    if st.button("🔄 Try Again"):
        st.session_state.clear()
        st.rerun()
