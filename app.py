import streamlit as st
import subprocess

# Function to run a script
def run_script(script_name):
    result = subprocess.run(["streamlit", "run", script_name], capture_output=True, text=True)
    st.text(result.stdout)
    st.text(result.stderr)

st.title('Run Multiple Python Streamlit Apps')

# Create buttons to run each script
if st.button('Run Basic Chat'):
    run_script('1.basic-chat.py')

if st.button('Run Chat with Input'):
    run_script('2.chat-with-input.py')

if st.button('Run Chat RAG Faiss'):
    run_script('3-1.chat-rag-faiss.py')

if st.button('Run Chat RAG OpenSearch Hybrid'):
    run_script('3-2.chat-rag-opensearch-hybrid.py')

if st.button('Run Chat SQL Agent'):
    run_script('4.chat-sql-agent.py')

if st.button('Run Chat SQL Tools'):
    run_script('5.chat-sql-tools.py')
