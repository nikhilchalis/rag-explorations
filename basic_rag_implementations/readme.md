# Basic Rag Implementation

![image](https://github.com/user-attachments/assets/5135767f-db4c-4c72-a944-fbfeef472ae5)


![image](https://github.com/user-attachments/assets/12835424-b191-4173-8409-a9c253259ab5)

This was a basic exploration of the simplest possible RAG using Ollama and LangChain (ChromaDB is included in LangChain)

The flow looks like this:

User Query -> Embedding Model -> Vector DB -> Relevant Docs -> Append top k docs to user query -> Send appended query to LLM (in this case Llama-3 8B) -> Return answer to user

The included ui.py gives a simple interface to interact with the program and runs the relevant files for you, included starting a powershell to run the Ollama server. This can cause issues if you already have an Ollama instance running
