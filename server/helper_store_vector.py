from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import Client, create_client
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os


embeddings = HuggingFaceEmbeddings()

async def upload_to_faiss(path):
    loader = PyPDFLoader(path)
    pages = loader.load_and_split()
    print("1st")
    supabase_url = os.environ.get('supabase_url')
    supabase_key = os.environ.get('supabase_key')
    supabase: Client = create_client(supabase_url, supabase_key)
    print("2nd")
    text_splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=0)
    docs = text_splitter.split_documents(pages)
    print("3rd")

    SupabaseVectorStore.from_documents(
        docs,
        embedding = embeddings,
        client=supabase,
        table_name="documents",
        query_name="match_documents",
        chunk_size=1024,
    )
    print(4)