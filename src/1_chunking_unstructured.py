
from pypdf import PdfReader

reader = PdfReader("data\Executive Summary.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

#print(text)

#---------------------------------------------------------------------------------

# 1. Character Text Splitting

# from langchain_core.documents import Document

# print("#### Character Text Splitting ####")

# # Manual Splitting
# chunks = []
# chunk_size = 35 # Characters
# for i in range(0, len(text), chunk_size):  # range(start,stop,step)
#     chunk = text[i:i + chunk_size]     #text[0:0+35]
#     chunks.append(chunk)
    
# #print(chunks)

# # for chunk in chunks:
# #     Document(page_content=chunk, metadata={"source": "local"})

# documents = [Document(page_content=chunk, metadata={"source": "local"}) for chunk in chunks]
# print(documents)

#---------------------------------------------------------------------------------


# # Automatic Text Splitting

from langchain_text_splitters import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size = 50, chunk_overlap=10, separator='', strip_whitespace=False)
documents = text_splitter.create_documents([text])
print(documents)


#---------------------------------------------------------------------------------

# 2. Recursive Character Text Splitting

# print("#### Recursive Character Text Splitting ####")

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# text_splitter = RecursiveCharacterTextSplitter(chunk_size = 65, chunk_overlap=10) # ["\n\n", "\n", " ", ""] 65,450
# documents = text_splitter.create_documents([text])
# print(documents) 


#---------------------------------------------------------------------------------

# # 3. Document Specific Splitting
# print("#### Document Specific Splitting ####")

# # Document Specific Splitting - Markdown
# from langchain_text_splitters import MarkdownTextSplitter
# markdown_text = """
# # Fun in California

# ## Driving

# Try driving on the 1 down to San Diego

# ### Food

# Make sure to eat a burrito while you're there

# ## Hiking

# Go to Yosemite
# """
# splitter = MarkdownTextSplitter(chunk_size = 40, chunk_overlap=0)
# documents = splitter.create_documents([markdown_text])
# print(documents)

#---------------------------------------------------------------------------------

# Document Specific Splitting - Python
# from langchain_text_splitters import PythonCodeTextSplitter
# python_text = """
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     self.code = code

# p1 = Person("John", 36)

# for i in range(10):
#     print (i)
# """
# python_splitter = PythonCodeTextSplitter(chunk_size=120, chunk_overlap=0)
# documents = python_splitter.create_documents([python_text])
# print(documents)

#---------------------------------------------------------------------------------
# 4. Semantic Chunking
# print("#### Semantic Chunking ####")

# from langchain_experimental.text_splitter import SemanticChunker
# from langchain_huggingface import HuggingFaceEmbeddings

# # Local embedding model
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# text_splitter = SemanticChunker(embeddings,breakpoint_threshold_type="percentile")

# documents = text_splitter.create_documents([text])

# print(documents)


#---- print("#### Agentic Chunking ####")------------------

# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("MISTRAL_API_KEY")
# #print(api_key)


# from langchain_mistralai import ChatMistralAI
# from pydantic import BaseModel
# from typing import List
# from langsmith import Client

# #obj = hub.pull("wfh/proposal-indexing")
# client = Client()
# prompt = client.pull_prompt("wfh/proposal-indexing")

# # LLM
# llm = ChatMistralAI(
#     model="mistral-small-latest",
#     temperature=0
# )

# runnable = prompt | llm

# # Pydantic schema
# class Sentences(BaseModel):
#     sentences: List[str]

# # Structured LLM
# structured_llm = llm.with_structured_output(Sentences)

# def get_propositions(text):
#     runnable_output = runnable.invoke({
#     	"input": text
#     }).content
    
#     # result = structured_llm.invoke(
#     #     f"Extract atomic propositions from the following text:\n{text}"
#     # )
#     result = structured_llm.invoke(runnable_output)
#     return result.sentences

# propositions = get_propositions(text)

# print(propositions)

# print("#### Agentic Chunking ####")

# from agentic_chunker import AgenticChunker
# ac = AgenticChunker()
# ac.add_propositions(propositions)
# print(ac.pretty_print_chunks())
# chunks = ac.get_chunks(get_type='list_of_strings')
# print(chunks)

# documents = [Document(page_content=chunk, metadata={"source": "local"}) for chunk in chunks]
# rag(documents, "agentic-chunks")