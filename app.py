import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Benim Yapay Zekam", page_icon="🤖")
st.title("Kişisel Yapay Zeka Botuma Hoş Geldin! 💬")

# 1. YEPYENİ ALDIĞIN API ANAHTARINI BURAYA YAZ (Tırnakları silme!)
GOOGLE_API_KEY = "AIzaSyB_mBFv0rNSdeFAZKYogHKENgNpdRk5l2w"
genai.configure(api_key=GOOGLE_API_KEY)

# 2. Google'ın şu anki en güncel ve kesin çalışan modelini çağırıyoruz
model = genai.GenerativeModel('gemini-2.0-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Bana bir şeyler yaz..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
