import streamlit as st
from debate_agent import get_counterargument, analyze_argument

st.title("🧠 Debate Coach AI (Open Source)")

user_input = st.text_area("💬 Enter your argument:", height=150)

if st.button("Submit"):
    if not user_input.strip():
        st.warning("Please enter an argument.")
    else:
        with st.spinner("Thinking..."):
            counter = get_counterargument(user_input)
            feedback = analyze_argument(user_input)

        st.subheader("🤖 Counterargument")
        st.write(counter)

        st.subheader("📊 Feedback")
        st.write(feedback)
