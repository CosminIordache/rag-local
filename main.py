from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.llms.ollama import Ollama
from langchain.memory import ConversationBufferMemory
from db.db import chroma_db

llm = Ollama(model="mistral")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# rag = ConversationalRetrievalChain.from_llm(
#     llm=llm, 
#     chain_type="stuff", 
#     retriever= chroma_db.as_retriever(),
#     verbose=True,
#     memory = memory
# )

rag2 = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever= chroma_db.as_retriever(),
    return_source_documents=True,
    verbose=True
)

# result = rag.invoke("explain the code")

# print("Question:", result['question']) 
# print("Answer:", result['answer']) 


result2 = rag2.invoke("explain the code")
print("Query: ", result2['query'])
print("Answer: ", result2['result'])