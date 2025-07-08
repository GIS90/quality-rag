# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    离线切词器，写入ChromaDB

base_info:
    __author__ = "PyGo"
    __time__ = "2025/7/3 23:23"
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
# usage: /usr/bin/python document_vectorization.py
# ------------------------------------------------------------
import os
from deploy.vector import VectorChromaDB
from deploy.spliter import Splitter
from deploy.config import (VECTOR_COLLECTION_NAME, DOCUMENT_LIST,
                           CHUNK_SIZE, CHUNK_OVERLAP)
from deploy.utils import get_vector_abs_path


def split_document_to_vector_db(db: VectorChromaDB, splitter: Splitter):
    for document in DOCUMENT_LIST:
        if not document: continue
        if not os.path.exists(document):
            print(f"{document}目录不存在，退出。。。。。。")
            os._exit(0)

        if (os.path.isfile(document)
                and (not document.endswith(".pdf") or not document.endswith(".txt") or not document.endswith(".md"))
        ):
            print(f"{document}文件类型不支持，退出。。。。。。")
            os._exit(0)

        splitter_documents = splitter.load_document(document)
        chunks = splitter.split_text(documents=splitter_documents)
        vector_documents = list()
        vector_metadatas = list()
        for chunk in chunks:
            if not chunk: continue
            vector_documents.append(chunk["txt"])
            vector_metadatas.append(chunk["metadata"])
        db.add(documents=vector_documents, metadatas=vector_metadatas)
        print(f"{document}->加入向量数据库成功")


db = VectorChromaDB(db_path=get_vector_abs_path(), collection_name=VECTOR_COLLECTION_NAME)
splitter = Splitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
split_document_to_vector_db(db, splitter)
print("文档向量初始化完成")

