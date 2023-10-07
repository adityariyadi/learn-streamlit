import streamlit as st

# Create storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prev chat hostory
st.write(st.session_state.messages)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask something")

# Display the message
if prompt:

    # Add user prompt in chat history
    st.session_state.messages.append({"role":"user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        st.write(prompt)

    # custom
    with st.chat_message("bot", avatar="😂"):
        st.write(prompt)

