from langchain_community.embeddings import LlamaCppEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents_chunks(documents):
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=300
    )
    return recursive_splitter.split_documents(documents)

def embed_documents(chunks):
    model = LlamaCppEmbeddings(model_path="/home/cosmin/Documents/models/mistral-7b-instruct-v0.1.Q5_K_M.gguf")
    return model.embed_documents([document.page_content for document in chunks])

    
    