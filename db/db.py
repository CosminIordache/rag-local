from langchain_community.vectorstores.chroma import Chroma 
from data.load_folder import load_folder
from data.DataFormat import split_documents_chunks, embed_documents


folder = "FOLDER PATH"
documents = load_folder(folder)
split_documents = split_documents_chunks(documents)
embeddings = embed_documents()

# Load the Chroma database from disk
chroma_db = Chroma(persist_directory="data-db", 
                   embedding_function=embeddings,
                   collection_name="test")

# Get the collection from the Chroma database
collection = chroma_db.get()

# If the collection is empty, create a new one
if len(collection['ids']) == 0:
    # Create a new Chroma database from the documents
    chroma_db = Chroma.from_documents(
        documents=split_documents, 
        embedding=embeddings, 
        persist_directory="data-db",
        collection_name="test"
    )

    # Save the Chroma database to disk
    chroma_db.persist()