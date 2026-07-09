# 🤖 AI Customer Support Agent

> A production-ready AI-powered Customer Support Agent built with LangChain, Retrieval-Augmented Generation (RAG), Groq LLM, FAISS, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-1.x-green)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![FAISS](https://img.shields.io/badge/Vector%20Database-FAISS-red)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-ff4b4b)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🌐 Live Application

**Live Demo:**  
https://customer-support-agent-johnsparz.streamlit.app/

**Demo Video:**  
*(Google Drive or YouTube link will be added here after recording the demonstration.)*

---

# 📌 Project Overview

Customer support teams spend significant time answering repetitive questions regarding company policies, pricing, refunds, working hours, and other frequently asked questions. Traditional chatbots often rely on hardcoded responses and cannot effectively retrieve information from company documents.

This project solves that problem by providing an AI-powered customer support assistant capable of:

- Answering company-specific questions using Retrieval-Augmented Generation (RAG)
- Searching the web for recent information
- Performing mathematical calculations
- Maintaining conversational context
- Delivering natural, human-like responses

The application was developed as the final capstone project for an AI Engineering Bootcamp.

---

# 🎯 Project Objectives

This project demonstrates the practical application of modern AI engineering by integrating:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- External AI tools
- Conversation memory
- Intelligent routing
- Production-ready software architecture

---

# ✨ Features

### Company Knowledge Assistant

Answers questions from a company handbook using:

- PDF document ingestion
- Semantic search
- FAISS vector database
- HuggingFace embeddings

Example:

> "What is the company's refund policy?"

---

### Web Search

Searches the internet using DDGS when information is unavailable locally.

Example:

> "Latest AI news"

---

### Calculator Tool

Performs accurate mathematical calculations without relying on the language model.

Example:

> "(250 × 18) + 900"

---

### Conversation Memory

Maintains chat history to support natural follow-up questions.

Example:

> User: What are your business hours?

> User: What about weekends?

---

### Intelligent Request Routing

Automatically routes requests to the appropriate component:

- General conversation
- RAG
- Calculator
- Web Search

---

# 🏗️ System Architecture

```
                    User
                     │
                     ▼
             Streamlit Interface
                     │
                     ▼
              Customer Agent
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Router      Memory     Prompt Builder
          │
  ┌───────┼──────────────┐
  ▼       ▼              ▼
RAG   Calculator     Web Search
  │       │              │
  └───────┼──────────────┘
          ▼
      ChatGroq (LLM)
          │
          ▼
       Final Response
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming Language |
| Streamlit | User Interface |
| LangChain 1.x | LLM Framework |
| ChatGroq | Large Language Model |
| FAISS | Vector Database |
| HuggingFace Embeddings | Semantic Embeddings |
| PyPDF | PDF Loading |
| RecursiveCharacterTextSplitter | Document Chunking |
| DDGS | Web Search |
| python-dotenv | Environment Variables |
| Logging | Monitoring & Debugging |

---

# 📂 Project Structure

```
customer-support-agent/
│
├── agent/
│   ├── customer_agent.py
│   ├── llm.py
│   ├── memory.py
│   ├── prompts.py
│   ├── response.py
│   └── router.py
│
├── rag/
│   ├── create_vectorstore.py
│   ├── loader.py
│   └── retriever.py
│
├── tools/
│   ├── calculator_tool.py
│   ├── retriever_tool.py
│   └── web_search_tool.py
│
├── utils/
│   ├── config.py
│   ├── constants.py
│   ├── exceptions.py
│   └── logger.py
│
├── data/
│   ├── company_handbook.pdf
│   └── vectorstore/
│
├── tests/
│
├── app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/johnsparz/customer-support-agent.git
```

Navigate into the project:

```bash
cd customer-support-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
GROQ_API_KEY=your_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

---

# 📄 Build the Vector Store

Before running the application, generate the FAISS vector index.

```bash
python -m rag.create_vectorstore
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 💬 Example Questions

### Company Questions

- What is the refund policy?
- What are your working hours?
- What benefits do employees receive?

### Calculator

- Calculate 875 × 46

### Web Search

- Latest AI news
- Who won the Champions League?

### General Conversation

- Tell me about your services.

---

# 🧠 AI Components Used

## Large Language Model

- ChatGroq
- Llama 3.3 70B Versatile

## Retrieval-Augmented Generation

- PyPDF
- Recursive Character Text Splitter
- HuggingFace Embeddings
- FAISS

## AI Tools

- Calculator Tool
- Web Search Tool
- Retriever Tool

## Memory

Modern LangChain message history implementation for maintaining conversational context.

---

# 🚀 Deployment

The application is designed for deployment on:

- Streamlit Community Cloud
- Hugging Face Spaces

---

# 📈 Future Improvements

- Multi-user authentication
- Persistent database-backed memory
- Conversation analytics dashboard
- Source citations for RAG responses
- Hybrid retrieval (BM25 + Vector Search)
- Docker support
- CI/CD pipeline
- Unit and integration test coverage

---

# 🎓 Capstone Submission

This project was developed as the final capstone for an AI Engineering Bootcamp.

### Submission Checklist

- ✅ Solves a real-world customer support problem
- ✅ Integrates a Large Language Model (Groq - Llama 3.3)
- ✅ Uses Retrieval-Augmented Generation (RAG)
- ✅ Includes multiple AI tools (Calculator, Web Search, PDF Retrieval)
- ✅ Supports conversational memory
- ✅ Publicly deployed using Streamlit Community Cloud
- ✅ Source code available on GitHub

### Live Application

https://customer-support-agent-johnsparz.streamlit.app/

### Demonstration Video

*To be added after recording.*

---

# 👨‍💻 Author

**John Arije**

Computer Science Graduate | AI Engineer | Machine Learning Engineer

GitHub: https://github.com/johnsparz

---

# 📄 License

This project is licensed under the MIT License.
