# PDF-RAG-Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to chat with PDF documents using local Large Language Models (LLMs).

## 🚀 Overview

This project enables users to upload PDF files and ask questions about their content. The application retrieves relevant information from the document and uses a local AI model to generate accurate responses.

## ✨ Features

- PDF document ingestion
- Text extraction from PDFs
- Document chunking

## 🚧 Planned Features

- Embedding generation
- Semantic search
- Vector database storage with ChromaDB
- Local LLM integration using Ollama
- Context-aware question answering

## 🛠️ Tech Stack

- Python
- Ollama
- LangChain
- ChromaDB
- PyPDF

## 📂 Project Structure

```text
pdf-rag-chatbot/
├── data/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## ⚙️ Installation

```bash
git clone https://github.com/TK-8055/pdf-rag-chatbot.git
cd pdf-rag-chatbot

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## 🎯 Learning Goals

- Understand Retrieval-Augmented Generation (RAG)
- Learn embeddings and vector databases
- Build an AI-powered document assistant
- Work with local LLMs using Ollama

## 📈 Development Progress

- [x] Project Setup
- [x] PDF Loading
- [x] Text Extraction
- [x] Chunking
- [ ] Embedding Generation
- [ ] ChromaDB Integration
- [ ] Retrieval Pipeline
- [ ] LLM Integration
- [ ] Chat Interface

## 🔮 Future Improvements

- Multi-PDF support
- Web UI
- Conversation memory
- Source citations
- Advanced retrieval techniques

## 📄 License

This project is licensed under the MIT License.
