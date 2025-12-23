import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from chatbot_stremlit import get_chat_chain  # Import your logic

st.set_page_config(page_title="Gemini Chat", page_icon="🧠")
st.title("My AI Assistant")

# Initialize the chain once and store it in session state
if "chain" not in st.session_state:
    st.session_state.chain = get_chat_chain()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display history
for message in st.session_state.chat_history:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# Chat Input
if query := st.chat_input("How can I help you?"):
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        # 1. Use .stream() instead of .invoke() logic
        # 2. st.write_stream automatically handles the generator loop
        full_response = st.write_stream(
            st.session_state.chain.stream({
                "chat_history": st.session_state.chat_history,
                "query": query
            })
        )
        st.markdown(full_response)

    # Update history
    st.session_state.chat_history.append(HumanMessage(content=query))
    st.session_state.chat_history.append(AIMessage(content=full_response))