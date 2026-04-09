
# 🎓 Smart Student RAG System

## 📌 Overview

This project is a **Retrieval-Augmented Generation (RAG)** application built using **Streamlit, LangChain, ChromaDB, and OpenAI**.

It allows users to:

* Upload student data from an Excel file
* Store it in a vector database (ChromaDB)
* Ask natural language questions
* Get intelligent answers using AI

---

## 🚀 Features

* 📊 Reads student data from Excel (`.xlsx`)
* 🧠 Converts data into embeddings using OpenAI
* 🔍 Stores data in Chroma vector database
* 💬 Ask questions like a chatbot
* ⚡ Fast and simple UI using Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* LangChain
* ChromaDB
* OpenAI API

---

## 📂 Project Structure

```
project/
│── app.py
│── students.xlsx
│── .env
│── requirements.txt
│── chroma_db/
```

---

## 🔑 Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/student-info-rag-app.git
cd student-info-rag-app
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Add OpenAI API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 📥 Ingest Data

Click:

```
📝 Ingest Excel Data
```

---

## 💬 Example Questions

* What course does Aarav Sharma study?
* What are the marks of student ID 10?
* Who scored highest in Python?
* Show details of Ananya Nair

---

## 📸 Demo Output

User enters a query → System retrieves relevant data → AI generates answer

---
