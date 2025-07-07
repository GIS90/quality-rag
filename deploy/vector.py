# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    向量数据库

base_info:
    __author__ = "PyGo"
    __time__ = "2025/7/3 22:09"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "quality-rag"

usage:

    def test():
        document = [
                "Python是一种解释型编程语言",
                "Python是世界上最好的语言",
                "Chroma是一个开源向量数据库",
                "PostgreSQL支持JSON和向量扩展",
                "Rust语言强调内存安全"
            ]

        db = VectorChromaDB(collection_name="T12")
        db.add(document)
        print(db.query("什么是ChromaDB"))


    test()

design:

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python vector.py
# ------------------------------------------------------------
import chromadb
from typing import Union, List
from chromadb.utils import embedding_functions

from deploy.config import VECTOR_DB_PATH

# 模型配置
from deploy.utils import get_model_embedding
MODEL_EMBEDDING = get_model_embedding()


class VectorChromaDB:
    def __init__(self,
                 db_path: str = VECTOR_DB_PATH,
                 collection_name: str = "VectorChromaDB",
                 collection_meta=None,
                 embedding_model: str = MODEL_EMBEDDING,    # 指定嵌入模型，不传入则使用配置的默认embedding模型
                                                            # 为何需要指定嵌入模型？保证向量数据库写入、查询的embedding模型统一，避免数据维度不一致导致错误
                 *args,
                 **kwargs) -> None:
        if len(collection_name) < 3:
            raise ValueError("Collection名称至少3个字符，支持A-Za-z0-9_组合")

        self.collection_name = collection_name
        if not collection_meta:
            collection_meta = {"description": collection_name}

        self.client = chromadb.PersistentClient(
            path=db_path,
            settings=chromadb.config.Settings(anonymized_telemetry=False)  # 关闭遥测
        )
        # 嵌入模型
        embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=embedding_model,
            device="cpu",
            normalize_embeddings=True
        )
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata=collection_meta,
            embedding_function=embedding_function
        )

    def reset(self):
        """
        重置
        """
        self.client.reset()

    def list_collection(self):
        return self.client.list_collections()

    def collection_count(self):
        return self.client.count_collections()

    def collection_peek(self):
        return self.collection.peek()

    def truncate_collection(self, collection_name: str):
        """
        清空数据集
        """
        collection = self.client.get_collection(collection_name)
        if collection:
            self.client.delete_collection(collection_name)

    def add(self, documents: list, ids: list = None, metadatas: list = None) -> bool:
        if not documents:
            return False

        if not ids:
            ids = [f"id{i}" for i in range(len(documents))]

        self.collection.add(
            documents=documents,
            ids=ids,
            metadatas=metadatas
        )
        return True

    def query(self, query_texts: Union[List, str], top: int = 5):
        texts = [query_texts] if isinstance(query_texts, str) else query_texts
        results = self.collection.query(
                query_texts=texts,
                n_results=top,
                include=["documents", "metadatas", "distances"]
            )
        _results = list()
        index = 1
        for doc, meta in zip(results["documents"][0], results["distances"][0]):
            _results.append({"text": doc, "value": meta, "top": index})
            index += 1
        return _results

