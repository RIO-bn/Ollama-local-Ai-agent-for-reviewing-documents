from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever


model = OllamaLLM(model="llama3.2")
template = """
You are an exeprt in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    question = input("ask your question: (q to quit)")
    if question == "q":
        break
    else :
        reviews = retriever.invoke(question)
        result = chain.invoke({"reviews": [], "question": question})
        print(result)