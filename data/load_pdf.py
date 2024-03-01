from langchain.document_loaders.pdf import PyPDFLoader

def load_pdf(filename):
    loader = PyPDFLoader(filename)
    documents = loader.load()
    return documents