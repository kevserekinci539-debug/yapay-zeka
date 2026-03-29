import streamlit as st
import google.generativeai as genai

# Sayfa tasarımı ve başlık
st.set_page_config(page_title="Benim Yapay Zekam", page_icon="🤖")
st.title("Kişisel Yapay Zeka Botuma Hoş Geldin! 💬")
st.markdown("Benim kodladığım bu asistanla istediğin her konuda sohbet edebilirsin.")

# API Bağlantısı (KENDİ ANAHTARINI BURAYA YAZ)
GOOGLE_API_KEY = "AIzaSyChhQV_SPiw-2VngJkVY-DTRltFkvbPaP8"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Sohbet geçmişini ekranda tutmak için hafıza ayarı
if "messages" not in st.session_state:
    st.session_state.messages = []

# Eski mesajları ekrana bas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcıdan gelen yeni mesajı al
if prompt := st.chat_input("Bana bir şeyler yaz..."):
    # Mesajı ekrana ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Yapay zekadan cevap al ve ekrana yazdır
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Bir hata oluştu. Lütfen API anahtarının doğru olduğundan emin ol!")
