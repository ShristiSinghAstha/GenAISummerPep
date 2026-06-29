from langchain_community.document_loaders import PyPDFLoader
data = PyPDFLoader("C:/Users/NISAN/OneDrive/Desktop/pepSummer/GENAIPEP/DocumentLoaders/notes.pdf")

docs = data.load()
print(docs)
