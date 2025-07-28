import streamlit as st
from openai import openAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🤖 AI Interview Coach")
st.write("Upload your resume or paste the text. Get instant feedback, tailored questions, and suggestions.")

resume_input = st.text_area("📄 Paste your resume text here:", height=300)
job_title = st.text_input("💼 What job are you applying for?", placeholder="e.g., Data Analyst")

if st.button("🧠 Analyze & Generate Questions") and resume_input and job_title:
    prompt = f"""
    You are an expert career coach and AI assistant.
    Analyze the resume below and generate:
    1. A short summary of the candidate's strengths
    2. 5 tailored interview questions for a {job_title} position
    3. Suggestions to improve the resume

    Resume:
    {resume_input}
    """

    with st.spinner("Analyzing resume and generating interview questions..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
    )
            output = response["choices"][0]["message"]["content"]
            st.markdown("### 📝 Results:")
            st.write(output)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
