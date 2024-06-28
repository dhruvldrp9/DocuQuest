from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import Client, create_client
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import os





def join_string(text):
    one_line_string = "".join(text.split("\n"))
    return one_line_string


def get_context(query):
    embeddings = HuggingFaceEmbeddings()
    supabase_url = os.environ.get('supabase_url')
    supabase_key = os.environ.get('supabase_key')
    supabase: Client = create_client(supabase_url, supabase_key)

    result = ""
    vector_store = SupabaseVectorStore(
        embedding=embeddings,
        client=supabase,
        table_name="documents",
        query_name="match_documents",
    )
    matched_docs = vector_store.similarity_search(query)

    for i, d in enumerate(matched_docs):
        result += d.page_content
        break
    
    return join_string(result)