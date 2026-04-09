import pandas as pd
import chromadb

# Read Excel
df = pd.read_excel("students.xlsx")

# Create client
client = chromadb.Client()

# 🔥 Delete old collection safely
try:
    client.delete_collection(name="students")
except:
    pass

# Create new collection
collection = client.get_or_create_collection("students")

# Insert data
for i, row in df.iterrows():
    text = f"Student {row['name']} studies {row['course']} and scored {row['marks']} marks"
    
    collection.add(
        documents=[text],
        ids=[str(i)]
    )

print("✅ Data ingestion completed!")