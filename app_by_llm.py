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

1、response_mode的选项，控制如何将检索到的文档整合到最终响应中：
    "compact" （默认）: 将检索到的文档合并后一次性生成响应。
    "refine" : 迭代优化答案（先对第一个文档生成响应，再用后续文档修正）。
    "tree_summarize" : 用树状结构汇总文档（适合长文本）。
    "no_text" : 仅返回检索到的文档节点，不生成回答。
    "accumulate" : 分别对每个文档生成回答后拼接。

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
from deploy.ai import RAGHuggingFaceAI, RAGOllamaAI

from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import streamlit as st
import os


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
Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = CHUNK_SIZE
Settings.chunk_overlap = CHUNK_OVERLAP

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
    similarity_top_k=TOP,               # 相似结果数量
    response_mode="tree_summarize",     # 响应模式，详情见usage
    streaming=False,                    # 流式输出
    verbose=False,                      # 详细输出
)

# ------------------------------
# web
# ------------------------------
st.title("📖 质量大Q智能问答RAG系统")
st.markdown("基于检索增强生成（RAG）的问答工具，无需上传文件，直接提问即可！")
st.text("请输入你的问题：")
col1, col2 = st.columns([4, 1])  # 第一列宽度占4/5，第二列占1/5
with col1:
    question = st.text_input(
        label="问题：",
        label_visibility="collapsed",
        placeholder="例如：wget命令可以做什么？"
    )
with col2:
    submit_button = st.button("提交")

if question and submit_button:
    print('>'*55 + 'start')
    response = query_engine.query(question)
    print(f"问题: {question}")
    print(f"回答: {response.response}")
    print('<'*55 + 'end')
    # response对象
    print(f"response.response: {response.response}")  # str	生成的答案文本（最常用）
    print(f"response.source_nodes: {response.source_nodes}")  # List[NodeWithScore]	检索到的源节点，包含文档片段和相似度得分
    print(f"response.metadata: {response.metadata}")  # dict	元数据（如模型名称、检索参数等）
    print(f"response.get_formatted_sources(): {response.get_formatted_sources()}")  # str	格式化后的参考来源（包含文本和出处）

    # 显示答案
    st.subheader("回答：")
    st.text(response.response)
    # 显示参考来源
    st.subheader("参考内容：")
    v_documents = []
    for i, doc in response.metadata.items():
        if doc.get("source") not in v_documents:
            v_documents.append(doc.get("source"))
            st.text(os.path.basename(doc.get("source")))


