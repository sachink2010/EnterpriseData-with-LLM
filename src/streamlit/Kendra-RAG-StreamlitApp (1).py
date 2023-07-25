import streamlit as st
from streamlit_chat import message
from typing import Dict
import json
from io import StringIO
from random import randint
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

import boto3
from langchain.llms.bedrock import Bedrock



st.set_page_config(page_title="Document Analysis (Model: Bedrock-Anthropic Claude-Instant)", page_icon=":robot:", layout="wide")
st.header("Chat with your Financial Documents- Annual Reports 📄")

boto3_bedrock = boto3.client("bedrock", 'us-east-1')

inference_modifier = {'max_tokens_to_sample':4096, 
                      "temperature":0.2,
                      "top_k":250,
                      "top_p":1,
                      "stop_sequences": ["Human:"]
                     }




@st.cache_resource
def load_chain():
    llm = Bedrock(model_id = "anthropic.claude-instant-v1",
                    client = boto3_bedrock, 
                    model_kwargs = inference_modifier 
                    )
    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=llm, memory=memory)
    return chain

# this is the object we will work with in the ap - it contains the LLM info as well as the memory
chatchain = load_chain()


# initialise session variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
    chatchain.memory.clear()
if 'widget_key' not in st.session_state:
    st.session_state['widget_key'] = str(randint(1000, 100000000))

# Sidebar - the clear button is will flush the memory of the conversation
st.sidebar.title("Sidebar")
clear_button = st.sidebar.button("Clear Conversation", key="clear")

if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['widget_key'] = str(randint(1000, 100000000))
    chatchain.memory.clear()


# this is the container that displays the past conversation
response_container = st.container()
# this is the container with the input text box
container = st.container()

#create lambda function KendraRetrievalLambda
lambda_client = boto3.client('lambda')

with container:
    # define the input text box
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("You:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

    # when the submit button is pressed we send the user query to Kendra to retrieve the relevant passages for user's query
    #  and later save the chat history
    if submit_button and user_input:
        params={ "user_query": user_input }

        #invoke lambda function KendraRAGLambda, get response and parse the response to a variable user_input_rag
        response = lambda_client.invoke(FunctionName='KendraRAGLambda',
                                        InvocationType='RequestResponse',
                                        Payload=json.dumps(params)
                                        )
        #Response Payload is in byte format, so we parse the response payload body to a variable kendra_rag
        json_response=response['Payload'].read()
        y = json.loads(json_response)
        kendra_rag=y['body']
        print("response is: " + str(kendra_rag))


        #Prompt to LLM= context (based on user_input) and relevant passages from Kendra+ "Question"- user_input+ "Answer:"

        user_input_rag=kendra_rag + """Question: """+str(user_input) + """Answer: """
                
        output = chatchain(user_input_rag)["response"]
        #st.text("output is: " + str(output)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
    
# this loop is responsible for displaying the chat history
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
