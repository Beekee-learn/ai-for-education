import streamlit as st 
from run import generate_response

st.image("static/logo_ai_for_ed.png", width=250)  # Adjust the width as needed
st.title("AI For Education Chatbot")
st.write('Welcome! I am your AI powered academic assistant, designed to support professors with research, course planning, general knowledge, and more. Ask me anything, and let’s enhance the learning experience together.')

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you in enhancing education today?"}]
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response, rag = generate_response(st.session_state.messages[-1]["content"])
            if rag == 0:
                st.markdown('<span style="color:red">response generated only using the Llama capacities, no context used</span>', unsafe_allow_html=True)
                st.write(response)
            else:
                st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
