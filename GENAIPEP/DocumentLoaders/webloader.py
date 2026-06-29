from langchain_community.document_loaders import WebBaseLoader
url = "https://www.oppo.com/in/about/"

data = WebBaseLoader(url)
docs = data.load()
print(len(docs))