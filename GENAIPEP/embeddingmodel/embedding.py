from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAIEmbeddings

embeddings = ChatOpenAIEmbeddings(model_name="text-embedding-3-small", dimensions=64)

vector = embeddings.embed_query("You are learning GEN AI")
print(vector)

