# from langchain.chat_models import ChatOpenAI 
# from langchain.schema import (SystemMessage,HumanMessage,AIMessage)
# from streamlit_chat import message
# import streamlit as st   
# from dotenv import load_dotenv 

# load_dotenv()

# chat = ChatOpenAI(model_name='gpt-3.5-turbo',temperature=0.5)

# if 'messages' not in st.session_state: 
#     st.session_state.messages = []

# st.set_page_config(
#     page_title='GPT-CUSTOM',
#     page_icon='icon'
# )

# st.subheader('AI GPT-TURBO Custom')

# with st.sidebar:
#     system_entered = st.text_input('System Role')
#     user_prompt = st.text_input('Send a Message')

#     if system_entered: 
#         if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
#             st.session_state.messages.append(SystemMessage(content=system_entered))

#     if user_prompt:
#         st.session_state.messages.append(HumanMessage(content=user_prompt))

#         with st.spinner('Working...'): 
#             response = chat(st.session_state.messages)
        
#         st.session_state.messages.append(AIMessage(content=response.content))

# st.session_state.messages



























from langchain.schema import ( HumanMessage, SystemMessage, AIMessage)
from langchain.chat_models import ChatOpenAI 
from dotenv import load_dotenv 
from streamlit_chat import message
import streamlit as st 

load_dotenv() 

chat = ChatOpenAI(model_name='gpt-3.5-turbo')

st.set_page_config(
    page_title='GPT-CUSTOM',
    page_icon='icon'
)

st.subheader('Your custom Chat GPT')

if 'messages' not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    system_message = st.text_input('System Role')
    user_prompt = st.text_input('Send a message')

    # System message 
    if system_message:
        # faça uma verificação dentro do SystemMessage para obter algum resultado de item adicionado a collection 
        if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
            st.session_state.messages.append(SystemMessage(content=system_message))

    # st.write(st.session_state.messages)

    # user prompt
    if user_prompt: 
        st.session_state.messages.append(HumanMessage(content=user_prompt))

        with st.spinner('Working on your request...'):
            response = chat(st.session_state.messages)
        
        st.session_state.messages.append(AIMessage(content=response.content))

if len(st.session_state.messages) >= 1:
    if not isinstance(st.session_state.messages[0], SystemMessage):
        st.session_state.messages.insert(0, SystemMessage(content='Your are a good assistent!'))

for i,msg in enumerate(st.session_state.messages[1:]):
    if i % 2 == 0:
        message(msg.content,is_user=True, key=f'{i} + cool')
    else: 
        message(msg.content, is_user=False, key=f'{i} + bad')