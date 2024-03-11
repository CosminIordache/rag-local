<div align="center" id="top"> 
  <h1>Local RAG using langchain & chromadb</h1>
</div>

## Instalation

For this simple RAG is using ollama like the LLM model and ollama embeddings to. You can use your local model .gguf, keep in mind that the processing cost for your computer will be heavier. 

The LLM model that you want to use is not a problem but as long as it meets those 2 requirements.

All the information will be saved locally, in a folder called data-db.

In this project you can upload (Folders, PDFs, and URLs).

### Ollama instalation & Ollama GitHub
```bash
https://ollama.com/download
```
```bash
https://github.com/ollama/ollama
```

### Install the requirements
```bash
pip install -r requirements.txt
```

Select the folder path and change the variable on the db.py file
folder = "FOLDER PATH"

When you have completed all these steps run the main.py file and see the MAGIC!
