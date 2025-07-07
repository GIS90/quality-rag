# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    main

base_info:
    __author__ = "PyGo"
    __time__ = "2025/7/3 23:13"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "quality-rag"

usage:

design:

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python main.py.py
# ------------------------------------------------------------
from deploy.utils import get_model_ai, get_model_embedding, get_vector_abs_path
from deploy.config import VECTOR_COLLECTION_NAME, TOP, CHUNK_SIZE, CHUNK_OVERLAP
from deploy.vector import VectorChromaDB
from deploy.ai import RAGHuggingFaceAI

from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings


# 模型配置
MODEL_EMBEDDING = get_model_embedding()
MODEL_AI = get_model_ai()


# ---------------------------------------------
# 配置本地大模型 > HuggingFace LLM
# ---------------------------------------------
llm = RAGHuggingFaceAI().llm

# ------------------------------
# 配置本地HuggingFace Embedding模型
# ------------------------------
embed_model = HuggingFaceEmbedding(model_name=MODEL_EMBEDDING)

# ------------------------------
# Llama-Index Core全局配置
# ------------------------------
Settings.llm = llm  # LLM
Settings.embed_model = embed_model  # Embedding模型
Settings.chunk_size = CHUNK_SIZE  # chunk_size
Settings.chunk_overlap =  CHUNK_OVERLAP  # chunk_overlap

# ------------------------------
# 加载持久化的ChromaDB索引
# ------------------------------
db = VectorChromaDB(db_path=get_vector_abs_path(), collection_name=VECTOR_COLLECTION_NAME)
vector_store = ChromaVectorStore(chroma_collection=db.collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# ------------------------------
# 向量加载 && 查询引擎
# ------------------------------
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
query_engine = index.as_query_engine(
    similarity_top_k=TOP,         # 返回最相似的3个结果
    response_mode="tree_summarize",    # 优化生成结果：tree_summarize compact
)

# ------------------------------
# 提问测试
# ------------------------------
question = "节日假期都什么？"
response = query_engine.query(question)
print(f"问题: {question}")
print(f"回答: {response}")
print('----------------------end')
