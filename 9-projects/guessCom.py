






# import streamlit as st
# import random
# import time

# st.title("🤖 AI Number Guesser 🎯")
# st.write("Think of a number between **1 and 100** and let the AI guess it!")

# # Initialize session state variables
# if "low" not in st.session_state:
#     st.session_state.low = 1
#     st.session_state.high = 100
#     st.session_state.comp_attempts = 0
#     st.session_state.comp_guess = None
#     st.session_state.message = ""
#     st.session_state.game_over = False

# if not st.session_state.game_over:
#     if st.button("🤔 Let AI Guess!"):
#         if st.session_state.low > st.session_state.high:
#             st.session_state.message = "❌ Oops! Something went wrong. Restart the game."
#         else:
#             with st.spinner("🤖 AI is thinking..."):
#                 time.sleep(1)  # Simulate AI thinking process
#                 st.session_state.comp_guess = random.randint(st.session_state.low, st.session_state.high)
#                 st.session_state.comp_attempts += 1
#                 st.session_state.message = f"🔮 AI guesses: **{st.session_state.comp_guess}**"

#     st.write(st.session_state.message)

#     if st.session_state.comp_guess:
#         feedback = st.radio(
#             "How was AI's guess?",
#             ["Too Low 👇", "Too High ☝", "Correct 🎯"],
#             index=2,
#         )

#         if st.button("✅ Submit Feedback"):
#             if feedback == "Too Low 👇":
#                 st.session_state.low = st.session_state.comp_guess + 1
#                 st.success("🔼 AI will guess a higher number next!")
#             elif feedback == "Too High ☝":
#                 st.session_state.high = st.session_state.comp_guess - 1
#                 st.warning("🔽 AI will guess a lower number next!")
#             else:
#                 st.session_state.game_over = True
#                 st.balloons()
#                 st.success(f"🎉 AI guessed your number in {st.session_state.comp_attempts} attempts!")

#     # Show progress bar of AI attempts
#     st.progress(min(st.session_state.comp_attempts / 10, 1.0))

# # Restart button
# if st.button("🔄 Restart Game"):
#     st.session_state.low = 1
#     st.session_state.high = 100
#     st.session_state.comp_attempts = 0
#     st.session_state.comp_guess = None
#     st.session_state.message = ""
#     st.session_state.game_over = False














import streamlit as st
import random
import time

st.title("🤖 AI Number Guesser 🎯")
st.write("Think of a number between **1 and 100**, and the AI will try to guess it!")

# Initialize session state
if "low" not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.comp_attempts = 0
    st.session_state.comp_guess = None
    st.session_state.game_over = False

# AI makes a guess
if not st.session_state.game_over:
    if st.session_state.comp_guess is None or "feedback_given" in st.session_state:
        with st.spinner("🤖 AI is thinking..."):
            time.sleep(1)  # Simulate AI thinking
            st.session_state.comp_guess = random.randint(st.session_state.low, st.session_state.high)
            st.session_state.comp_attempts += 1
            st.session_state.feedback_given = False  # Reset feedback flag

# Display AI's current guess
if st.session_state.comp_guess:
    st.subheader(f"🤖 AI's Guess: **{st.session_state.comp_guess}**")

# User feedback section
if not st.session_state.game_over:
    feedback = st.radio(
        "How was AI's guess?",
        ["Too Low 👇", "Too High ☝", "Correct 🎯"],
        index=2,
        key="feedback"
    )

    if st.button("✅ Submit Feedback"):
        if feedback == "Too Low 👇":
            st.session_state.low = st.session_state.comp_guess + 1
            st.success("🔼 AI will guess a higher number next!")
        elif feedback == "Too High ☝":
            st.session_state.high = st.session_state.comp_guess - 1
            st.warning("🔽 AI will guess a lower number next!")
        else:
            st.session_state.game_over = True
            st.balloons()
            st.success(f"🎉 AI guessed your number **{st.session_state.comp_guess}** in {st.session_state.comp_attempts} attempts!")

        st.session_state.feedback_given = True
        st.rerun()  # Refresh UI to show the next guess immediately

# Show progress bar based on attempts
st.progress(min(st.session_state.comp_attempts / 10, 1.0))

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.comp_attempts = 0
    st.session_state.comp_guess = None
    st.session_state.game_over = False
    st.rerun()
