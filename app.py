import streamlit as st

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.markdown(
    """
    <h1 style='text-align: center; color: yellow;'>Hello !!</h1>
    <h2 style='text-align: center; color: skyblue;'>- An AI Chat-bot 😁</h2>
    <h4 style='text-align: center;'>Choose one of the options below</h4>
    """,
    unsafe_allow_html=True,
)

st.page_link("pages/1_📄_PDF_to_AI_Chatbot.py", label="📄 PDF to AI Chat-bot")
st.page_link("pages/2_💬_Chat_with_Me.py", label="💬 Chat with Me")