import streamlit as st 
from run import generate_response

st.link_button("Back", url="http://beekeeai.local:5000")
st.image("static/logo.png", width=150)  # Adjust the width as needed
st.title("Beekee Bot")
st.write('Hello, I am your general knowledge assistant. Ask me anything!')

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]
    
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
            response = generate_response(st.session_state.messages[-1]["content"])
            if response[1] == 0:
                st.write(response[0])
                st.markdown('<span style="color:red">response generated only using the Llama capacities, no context used</span>', unsafe_allow_html=True)
            else:
                st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
