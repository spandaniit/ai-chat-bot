import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Chat with Me", page_icon="💬")
st.title("💬 Chat with Me")

if st.button("🔙 Back to Home"):
    st.switch_page("app.py")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Say something...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state["messages"]
    )
    bot_reply = response.choices[0].message["content"]
    st.chat_message("assistant").markdown(bot_reply)
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})