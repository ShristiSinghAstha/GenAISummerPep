from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

data = TextLoader(
    "C:/Users/NISAN/OneDrive/Desktop/pepSummer/GENAIPEP/DocumentLoaders/notes.txt"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=5
)

docs = data.load()
chunks = splitter.split_documents(docs)

for i in chunks:
    print(i.page_content)
    print()
    