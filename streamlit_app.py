import streamlit as st
import openai

# Set your OpenAI key (better: use secrets.toml or environment variable)
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "sk-..."

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

    with st.spinner("Analyzing resume and generating questions..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        output = response["choices"][0]["message"]["content"]

    st.markdown("### 📝 Results:")
    st.write(output)
