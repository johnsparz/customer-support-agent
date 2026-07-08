# AI Customer Support Agent

A production-ready AI Customer Support Agent built with **LangChain**, **Groq**, **FAISS**, **RAG**, and **Streamlit**.

## Overview

This project is an AI-powered customer support assistant that answers company-related questions using Retrieval-Augmented Generation (RAG), performs mathematical calculations, searches the web for recent information, and maintains conversation history.

It was developed as a final AI Engineering Bootcamp capstone project using modern LangChain 1.x architecture.

---

## Features

- Company knowledge retrieval using RAG
- FAISS vector database
- HuggingFace sentence embeddings
- Groq LLM (Llama 3.3)
- Intelligent request routing
- Conversation memory
- Calculator tool
- Web search using DDGS
- Streamlit chat interface
- Modular, production-style architecture
- Logging and configuration management

---

## Tech Stack

- Python 3.12
- Streamlit
- LangChain 1.x
- langchain-core
- langchain-community
- langchain-huggingface
- langchain-text-splitters
- FAISS
- sentence-transformers
- Groq API
- DDGS
- PyPDF
- python-dotenv

---

## Project Structure

```text
customer-support-agent/
│
├── agent/
├── rag/
├── tools/
├── utils/
├── data/
├── tests/
├── app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## Architecture

```
User
   │
   ▼
Streamlit UI
   │
   ▼
CustomerAgent
   │
   ▼
Router
   │
   ├───────────────┐
   ▼               ▼
RAG          Calculator
   │               │
   └───────┬───────┘
           ▼
      Web Search
           │
           ▼
       ChatGroq LLM
           │
           ▼
        Response
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/johnsparz/customer-support-agent.git
```

Move into the project directory:

```bash
cd customer-support-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file from `.env.example`.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Create the Vector Store

Before running the application, build the FAISS index:

```bash
python -m rag.create_vectorstore
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Example Questions

- What is the company refund policy?
- What are the working hours?
- Calculate 245 * 18
- What happened in AI today?
- Tell me about employee benefits.

---

## Future Improvements

- Multi-user chat sessions
- Persistent memory
- Citation support
- Hybrid search
- Authentication
- Docker deployment
- CI/CD pipeline

---

## License

This project is licensed under the MIT License.
