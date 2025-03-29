import streamlit as st
import time

# Initialize session state
if "countdown" not in st.session_state:
    st.session_state.countdown = 0
    st.session_state.running = False

st.title("⏳ Countdown Timer")

# User input for countdown time
seconds = st.number_input("⏰ Enter countdown time (seconds):", min_value=1, step=1)

# Start & Reset buttons
col1, col2 = st.columns(2)
if col1.button("▶ Start"):
    st.session_state.countdown = seconds
    st.session_state.running = True

if col2.button("🔄 Reset"):
    st.session_state.running = False
    st.session_state.countdown = 0

# Countdown logic
while st.session_state.running and st.session_state.countdown > 0:
    mins, secs = divmod(st.session_state.countdown, 60)
    st.subheader(f"⏳ Time Left: {mins:02d}:{secs:02d}")
    st.progress((seconds - st.session_state.countdown) / seconds)
    time.sleep(1)
    st.session_state.countdown -= 1
    st.rerun()

# Show message when time’s up
if st.session_state.countdown == 0 and st.session_state.running:
    st.success("🎉⏰ Time’s up! ⏰🎉")
    st.session_state.running = False
