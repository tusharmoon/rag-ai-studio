from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Loading the PDF using PDF Loader of Langchain
loader = PyPDFLoader('data\Executive Summary.pdf')
docs = loader.load()
print(len(docs))
# print(docs[0].page_content)
# print(docs[1].metadata)


#--------------------- Splitting 1-----------------
# text_splitter = CharacterTextSplitter(chunk_size = 50, chunk_overlap=10, separator='', strip_whitespace=False)
# documents = text_splitter.split_documents(docs)
# print(documents)

#--------------------- Splitting 2-----------------
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 65, chunk_overlap=10) # ["\n\n", "\n", " ", ""] 65,450
documents = text_splitter.split_documents(docs)
print(documents) 




# When you want to load multuple files---->
# from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# loader = DirectoryLoader(
#     path='books',
#     glob='*.pdf',
#     loader_cls=PyPDFLoader
# )

# docs = loader.lazy_load()

# for document in docs:
#     print(document.metadata)


# CSV File Loader
# from langchain_community.document_loaders import CSVLoader

# loader = CSVLoader(file_path='Social_Network_Ads.csv')

# docs = loader.load()

# print(len(docs))
# print(docs[1])