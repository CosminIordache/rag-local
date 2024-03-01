from langchain.document_loaders.web_base import WebBaseLoader

def load_url(url):
    loader = WebBaseLoader(url)
    documents = loader.load()

