import streamlit as st
from mailpro import ask_mailpro

st.set_page_config(
    page_title="MailPro – Business Email Assistant",
    page_icon="📧"
)

st.title("📧 MailPro")
st.caption("Professional business email assistant (Python 3.13 compatible)")

if "history" not in st.session_state:
    st.session_state.history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Write, reply, summarize, or save an email")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant"):
        response = ask_mailpro(user_input, st.session_state.history)
        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.session_state.history.append({
        "role": "user",
        "content": user_input
    })
    st.session_state.history.append({
        "role": "assistant",
        "content": response
    })