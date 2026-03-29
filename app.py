import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Benim Yapay Zekam", page_icon="🤖")
st.title("Kişisel Yapay Zeka Botuma Hoş Geldin! 💬")

# YENİ API Anahtarını Buraya Yaz
GOOGLE_API_KEY = "AIzaSyB_dORdtYw3A65trWq_cH0M4CPhCOLD7n8"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

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
        # Hata gizleme kısmını kaldırdık, artık sistemi doğrudan çalıştırıyoruz
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
