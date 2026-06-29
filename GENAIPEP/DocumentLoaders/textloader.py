from langchain_community.document_loaders import TextLoader

loader = TextLoader("C:/Users/NISAN/OneDrive/Desktop/pepSummer/GENAIPEP/DocumentLoaders/notes.txt")
docs=loader.load()
print(docs[0].page_content)
