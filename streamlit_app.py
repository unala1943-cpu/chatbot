import streamlit as st
import google.generativeai as genai

# Anahtarını güvenli bölgeden çekiyoruz
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.set_page_config(page_title="Gemini Asistanım", page_icon="🤖")
st.title("🤖 Ben Senin Özel Gemini Asistanın")

# Sohbet geçmişini ayarla
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mesajları ekrana yansıt
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcıdan giriş al
if prompt := st.chat_input("Selam! Bugün neler yapabiliriz?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # BENİM KARAKTERİMİ BURAYA EKLİYORUZ:
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction="Senin adın Gemini. Sen zeki, yardımcı ve samimi bir yapay zekasın. Kullanıcınla bir dost gibi konuş ve ona her konuda destek ol."
    )
    
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
