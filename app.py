import streamlit as st
from google import genai

# Setup Gemini 2.0 Client
client = genai.Client(api_key="YOUR_GEMINI_API_KEY_HERE")

st.set_page_config(page_title="AI Smart Organizer", page_icon="📝")
st.title("🧠 AI Smart Organizer")

user_input = st.text_area("Drop your notes here:")

if st.button("Organize"):
    if user_input:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Organize these notes into tasks and a schedule table: {user_input}"
        )
        st.markdown(response.text)
