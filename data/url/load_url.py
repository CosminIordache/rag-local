from langchain.document_loaders.web_base import WebBaseLoader

loader = WebBaseLoader("https://github.com/basecamp/handbook/blob/master/37signals-is-you.md")
documents = loader.load()

print(len(documents))

print(documents)
