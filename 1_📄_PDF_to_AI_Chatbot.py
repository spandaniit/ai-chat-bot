import streamlit as st
import fitz
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="PDF Chatbot", page_icon="📄")
st.title("📄 Chat with your PDF")

if st.button("🔙 Back to Home"):
    st.switch_page("app.py")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    raw_text = ""
    for page in doc:
        raw_text += page.get_text()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(raw_text)
    documents = [Document(page_content=chunk) for chunk in chunks]

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )

    st.success("✅ PDF loaded! Ask a question.")
    query = st.text_input("Ask something about the PDF")
    if query:
        result = qa_chain({"query": query})
        st.markdown(f"Answer: {result['result']}")