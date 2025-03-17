import os
import streamlit as st
import random
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings


OPENAI_API_KEY = "***"

# Load and split the PDF into chunks
def split_pdf_into_chunks(uploaded_file):
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    loader = PyPDFLoader(temp_file_path)
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, separators=["\n\n", ".", "!", "?"]
    )
    chunks = text_splitter.split_documents(pages)
    return chunks

# Store document chunks in FAISS vector store
def create_faiss_index(chunks):
    embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY) #Converts text chunks into numerical vectors using OpenAI's embedding model
    vectorstore = FAISS.from_documents(chunks, embedding_model) #Stores the vectorized text in a FAISS database.
    return vectorstore #This helps retrieve relevant information quickly when a user asks a question.

# Retrieve most relevant chunks from FAISS
def retrieve_relevant_chunks(vectorstore, query, top_k=3):
    docs = vectorstore.similarity_search(query, k=top_k) #Searches for top-k most relevant text chunks based on the query.
    return "\n\n".join([doc.page_content for doc in docs]) #Converts retrieved chunks into a single text string.

# Generate questions and answers based on retrieved content
def generate_questions_answers(query, grade, question_type, num_questions, vectorstore):
    relevant_text = retrieve_relevant_chunks(vectorstore, query) #Uses the retrieved relevant text as context.

    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY) #Asks GPT-3.5 to generate both questions & answers based on that context.

    prompt = f"""
    Based on the following content, generate {num_questions} {question_type} questions for Grade {grade} students. 
    Also, provide the correct answer for each question.
    
    {relevant_text}
    
    Format:
    1. Question?
       a) Option 1
       b) Option 2
       c) Option 3
       d) Option 4
       Answer: b) [Correct Option]
    """

    response = llm([HumanMessage(content=prompt)])
    return response.content.strip()

# Streamlit UI
st.title("📘 PDF-Based Question & Answer Generator with FAISS")
st.write("Upload a PDF and generate AI-powered questions with answers.")

pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
grade = st.selectbox("Select Grade", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
question_type = st.selectbox("Type of Questions", ["MCQ", "One Word", "Logical Reasoning", "Fill in the Blanks"])
num_questions = st.slider("Number of Questions", 1, 50, 20)
query = st.text_input("Enter a topic or keyword to focus on (optional)")

if st.button("Generate Questions & Answers"):
    if pdf_file:
        with st.spinner("Processing the PDF..."):
            chunks = split_pdf_into_chunks(pdf_file)
            vectorstore = create_faiss_index(chunks)

        with st.spinner("Generating questions and answers..."):
            questions_answers = generate_questions_answers(query, grade, question_type, num_questions, vectorstore)

        st.success("✅ Questions & Answers generated successfully!")
        st.text_area("Generated Questions & Answers", value=questions_answers, height=500)
    else:
        st.warning("⚠️ Please upload a PDF.")
