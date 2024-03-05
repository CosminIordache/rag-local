from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents_chunks(documents):
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50
    )
    return recursive_splitter.split_documents(documents)

def embed_documents():
    model = OllamaEmbeddings(model="mistral")
    return model