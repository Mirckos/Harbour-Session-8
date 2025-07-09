import streamlit as st

if "hits" not in st.session_state:
    st.session_state.hits = 0
st.session_state.hits += 1
st.write("Page views:", st.session_state.hits)

# Simple echo chat
for m in st.session_state.get("dialog", []):
    st.chat_message(m["role"]).write(m["text"])

if q := st.chat_input("Say something"):
    st.session_state.dialog = st.session_state.get("dialog", [])
    st.session_state.dialog.append({"role": "user", "text": q})
    st.chat_message("assistant").write(q[::-1])
