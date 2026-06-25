from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

texts=[
    "Hello I am Shristi S Astha",
    "I am good",
    "Currently learning genai"
]
vector = embeddings.embed_documents(texs)
#print(vector)
print(len(vector[0]))
