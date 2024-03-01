from langchain_community.vectorstores.qdrant import Qdrant
from data.load_folder import load_folder
from data.DataFormat import split_documents_chunks, embed_documents

folder = "/home/cosmin/VSCode/git_backend"
documents = load_folder(folder)
split_documents = split_documents_chunks(documents)
embeddings = embed_documents(split_documents)

print(split_documents)
print("-------------------------------------------------------------------------------")
print(embeddings)