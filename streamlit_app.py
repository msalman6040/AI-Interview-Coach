import openai
import streamlit as st

openai.api_key = "your-openai-key"

st.title("AI interview coach")

resume_text = st.text_area("paste your resume text:")
job_title = st.text-input("what job are you applying for?")

if st.button("Analyze and generate Questions"):
  prompt = f"""
  you are an expert career coach. Analyze the following resume and generate:
  1. A summary of the candidate's strengths.
  2. 5 tailored interview questions for a {job_title} position
  3. Suggestions to improve their resume.
  resume: {resume_text}
  """

  response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[{"role": "user", "content": prompt}]      
  )
  st.write(response['choices'][0]['message']['content'])
