import streamlit as st
import google.generativeai as genai

# Gemini anahtarını ayarlardan alıyoruz
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.set_page_config(page_title="Gemini Sohbet Botu", page_icon="🤖")
st.title("🤖 Selam! Ben Senin Özel Gemini Asistanın")

# Sohbet geçmişini sakla
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mesajları ekrana yaz
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcıdan soru al
if prompt := st.chat_input("Bana bir şeyler sor..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini'den cevap al
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
