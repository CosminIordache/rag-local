from langchain.document_loaders.pdf import PyPDFLoader
loader = PyPDFLoader("/home/cosmin/VSCode/rag/data/PDF/T2 - Almacenamiento de datos masivos.pdf")
documents = loader.load()

# number of pages of the pdf
print(len(documents))

# page_content & metadata
print(documents)