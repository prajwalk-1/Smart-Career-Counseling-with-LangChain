import streamlit as st
from resume_parser import extract_resume_text, analyze_resume
from career_logic import career_chat, generate_mock_interview

# Streamlit configuration
st.set_page_config(page_title="Career Counseling Chatbot", layout="wide")

# Title
st.title("Career Counseling Chatbot")
st.write("Get career advice, resume feedback, and mock interview preparation.")

# Tabs
tab1, tab2, tab3 = st.tabs(["Career Advice", "Resume Analysis", "Mock Interview"])

# Career Advice
with tab1:
    st.header("Career Advice")
    user_input = st.text_input("Ask your career-related question:")
    if st.button("Get Advice"):
        if user_input:
            response = career_chat(user_input)
            st.text_area("AI Response", response, height=200)

# Resume Analysis
with tab2:
    st.header("Resume Analysis")
    uploaded_file = st.file_uploader("Upload your resume (PDF format):")
    if uploaded_file:
        resume_text = extract_resume_text(uploaded_file)
        feedback = analyze_resume(resume_text)
        st.subheader("Analysis Results")
        st.write(f"Word Count: {feedback['word_count']}")
        st.write("Suggestions:")
        for suggestion in feedback["suggestions"]:
            st.write(f"- {suggestion}")

# Mock Interview
with tab3:
    st.header("Mock Interview")
    industry = st.selectbox("Select Industry", ["Technology", "Finance", "Healthcare", "Education"])
    if st.button("Generate Mock Interview"):
        if industry:
            mock_interview = generate_mock_interview(industry)
            st.text_area("Mock Interview", mock_interview, height=300)
