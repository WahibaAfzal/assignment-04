import streamlit as st
# Streamlit UI
st.title("🎭 Fun Mad Libs Game! 🚀")
st.write("Fill in the blanks and create a hilarious story!")

# Input fields
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adjective = st.text_input("Enter an adjective:")
place = st.text_input("Enter a place:")

# Button to generate the story
if st.button("Generate Story"):
    if noun and verb and adjective and place:
        story = f"One day, a {adjective} {noun} decided to {verb} at {place}. It was an amazing adventure! 😄"
        st.subheader("Your Mad Libs Story:")
        st.success(story)  # Display the story with a success message
    else:
        st.error("Please fill all the blanks to create your story!")  # Error message if fields are empty

# Footer
st.markdown("---")


