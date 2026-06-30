import streamlit as st
import requests

st.set_page_config(page_title='Jaggu Deepu AI', page_icon='🧠')
st.title('🧠 Jaggu Deepu AI')
st.caption('Your Personal AI Assistant')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

if prompt := st.chat_input('Ask Jaggu Deepu AI anything...'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message('assistant'):
        with st.spinner('Jaggu Deepu is thinking...'):
            try:
                response = requests.post(
                    'http://localhost:8000/chat',
                    json={'message': prompt}
                )
                reply = response.json()['reply']
            except Exception as e:
                reply = f'Error: {str(e)}'
            st.markdown(reply)

    st.session_state.messages.append({'role': 'assistant', 'content': reply})
