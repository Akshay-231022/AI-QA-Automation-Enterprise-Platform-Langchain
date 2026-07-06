from langchain_community.vectorstores import FAISS

from config import embedding_model


def create_vector_store(chunks):
    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store