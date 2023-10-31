import streamlit as st

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    st.session_state['disable_input'] = False
    
def show_messages() :
    for message in st.session_state['messages'] :
        with st.chat_message(message['role']) :
            st.write(message['content'])
    
# while True :
user = st.chat_input("Enter message ...", disabled=st.session_state.disable_input)
if user :        
    st.session_state.disable_input = True
    
    st.session_state['messages'].append({"role":"user", "content":user})
    
    assistant = "YO it's me assistant"
    st.session_state['messages'].append({"role":"assistant", "content":assistant})
    
    show_messages()
    st.session_state.disable_input = False