from langchain.chains import RetrievalQA
from langchain.llms.ollama import Ollama
from db.db import chroma_db

llm = Ollama(model="mistral")

rag = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever= chroma_db.as_retriever(),
    return_source_documents=True,
    verbose=True
)

result = rag.invoke("explain the code")
print(result['result'])
