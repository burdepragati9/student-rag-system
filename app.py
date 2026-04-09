# app.py
import streamlit as st
from dotenv import load_dotenv
import os
import pandas as pd
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate

# ----------------------------
# 1️⃣ Load environment variables
# ----------------------------
load_dotenv(dotenv_path="./.env")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")  # ✅ Correct

if not OPENAI_KEY:
    st.error("❌ OpenAI API key not found. Please set OPENAI_API_KEY in .env")
    st.stop()

# ----------------------------
# 2️⃣ Initialize embeddings and Chroma
# ----------------------------
embedding = OpenAIEmbeddings(api_key=OPENAI_KEY)

vectordb = Chroma(
    collection_name="students",
    embedding_function=embedding,
    persist_directory="./chroma_db"
)

# ----------------------------
# 3️⃣ Initialize LLM
# ----------------------------
llm = ChatOpenAI(temperature=0, api_key=OPENAI_KEY)

# ----------------------------
# 4️⃣ Prompt template
# ----------------------------
prompt_template = """
You are a helpful student information assistant. 
Based on the following context, answer the question:

Context: {context}

Question: {question}

Answer:
"""
prompt = PromptTemplate.from_template(prompt_template)

# ----------------------------
# 5️⃣ Streamlit UI
# ----------------------------
st.title("🎓 Smart Student RAG System")

query = st.text_input("Ask anything about students:")

if st.button("🔍 Search"):
    if query:
        with st.spinner("Processing..."):
            # 🔹 Query Chroma collection directly
            results = vectordb._collection.query(
                query_texts=[query],
                n_results=3  # top 3 results
            )
            docs = [doc for doc in results['documents'][0]]

            if not docs:
                st.warning("No relevant student records found.")
            else:
                # Combine documents into context
                context = "\n".join(docs)
                final_prompt = prompt.format(context=context, question=query)

                # Generate answer from LLM
                answer = llm(final_prompt)
                st.success("Answer:")
                st.write(answer)
    else:
        st.warning("Please enter a question")

# ----------------------------
# 6️⃣ Button to ingest Excel data
# ----------------------------
if st.button("📝 Ingest Excel Data"):
    try:
        df = pd.read_excel("students.xlsx")

        # Optional: Replace 'You' with your name in 'Owned by'
        YOUR_NAME = "Pragati Burde"
        if 'owned by' in df.columns:
            df['owned by'] = df['owned by'].apply(lambda x: YOUR_NAME if str(x).strip().lower() == "you" else x)

        # Clear old collection
        try:
            vectordb._collection.delete()
        except:
            pass

        for i, row in df.iterrows():
            text = (
                f"Owned by: {row.get('owned by','')}, "
                f"Name: {row.get('name','')}, "
                f"Project: {row.get('project','')}, "
                f"Permission: {row.get('permission','')}"
            )
            vector = embedding.embed_query(text)
            vectordb._collection.add(
                documents=[text],
                ids=[str(i)],
                embeddings=[vector]
            )
        st.success("✅ Excel data ingested successfully!")
    except Exception as e:
        st.error(f"Error ingesting Excel: {e}")