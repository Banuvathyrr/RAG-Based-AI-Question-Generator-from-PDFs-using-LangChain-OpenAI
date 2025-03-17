# RAG based AI Question Generator from PDFs using LangChain OpenAI
A RAG-based AI Question Generator that extracts relevant content from PDFs using FAISS vector search and generates questions with OpenAI's LLM. This system enables dynamic quiz creation based on user-selected topics and grade levels.

🚀 Overview
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project is a Retrieval-Augmented Generation (RAG)-based AI-powered question generator that extracts relevant content from PDFs using FAISS vector search and generates questions with OpenAI's LLM. The system dynamically creates quizzes based on user-selected topics and grade levels.


![image](https://github.com/user-attachments/assets/d685844d-236a-4c4f-944e-8968bd694dc8)


🎯 Features
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
📂 PDF Upload: Users can upload a PDF containing study material.

🔍 Retrieval-Based Question Generation: FAISS is used to retrieve the most relevant content from the PDF.

🤖 AI-Powered Question Generation: OpenAI's GPT-3.5-turbo generates questions from the extracted content.

🏫 Grade-Based Filtering: Supports question generation for different grade levels.

🎯 Multiple Question Types: Generates MCQs, logical reasoning, one-word answers, and fill-in-the-blanks.

🎨 User-Friendly UI: Built with Streamlit for an intuitive experience.

📜 How It Works
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Upload a PDF – Users upload study material.

Document Chunking – The PDF is split into meaningful chunks.

Embedding & Vectorization – FAISS stores the document embeddings for efficient retrieval.

Query Processing – User provides a topic or keyword to focus on.

Retrieval – FAISS finds the most relevant chunks from the document.

Question Generation – OpenAI’s LLM generates questions based on the retrieved content.

Display Results – Generated questions are shown in the Streamlit interface.

🛠️ Tech Stack
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Programming Language: Python 🐍

Framework: Streamlit 🎨

Document Processing: LangChain 📄

Vector Database: FAISS 🧠

LLM: OpenAI GPT-3.5-turbo 🤖


📝 License
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project is licensed under the MIT License.

🌟 Acknowledgments
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
OpenAI for GPT-3.5

LangChain for document processing

FAISS for efficient similarity search
