# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    切词

base_info:
    __author__ = "PyGo"
    __time__ = "2025/7/3 22:09"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "quality-rag"

usage:
    def test():
        splitter = Splitter(chunk_size=200, chunk_overlap=30)
        # 1. 加载文档
        pdf_documents = splitter.load_document("E:/project-ai/quality-rag/datas/Tiancom-R-002考勤、请假、休假管理规定-2025.pdf")
        # 2. 切分文本
        chunks = splitter.split_text(documents=pdf_documents)
        # 3. 分析切分结果
        splitter.analyze_chunks(chunks)


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
# usage: /usr/bin/python spliter.py
# ------------------------------------------------------------
import os
from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (PyPDFLoader, TextLoader, UnstructuredMarkdownLoader,
                                                  DirectoryLoader)
from langchain_huggingface import HuggingFaceEmbeddings

# 模型配置
from deploy.utils import get_model_embedding
MODEL_EMBEDDING = get_model_embedding()


class Splitter:
    def __init__(self, chunk_size=200, chunk_overlap=25):
        """
        :param chunk_size: 每个文本块的最大字符数
        :param chunk_overlap: 块之间的重叠字符数

        采用本地embedding模型
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", "。", "！", "？", "；", "……", " ", ""],  # 中文分隔符
            length_function=len,
            is_separator_regex=False
        )
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=MODEL_EMBEDDING,
            model_kwargs={'device': 'cpu'}
        )

    def load_document(self, file_path: str):
        """
        加载文档内容
        :param file_path:
            - 文件路径（支持PDF/TXT/MD）
            - 文件目录
        :return: 文档内容列表
        """
        if not os.path.exists(file_path):
            return FileNotFoundError(f"文件 {file_path} 不存在")

        if os.path.isdir(file_path):
            loader = DirectoryLoader(
                file_path,
                glob=["**/*.md", "**/*.txt", "**/*.pdf"],
                show_progress=True,  # 显示加载进度
                use_multithreading=True,  # 多线程加载
            )
        else:
            if file_path.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
            elif file_path.endswith('.txt'):
                loader = TextLoader(file_path, encoding='utf-8')
            elif file_path.endswith('.md'):
                loader = UnstructuredMarkdownLoader(file_path)
            else:
                return NotImplementedError("仅支持PDF和TXT格式")

        content = list()
        for page in loader.load():
            content.append({
                "content": page.page_content,
                "metadata": page.metadata
            })
        return content

    def split_text(self, documents: List[Dict]) -> List[Dict]:
        """
        切分文档为适合RAG处理的文本块
        :param documents: 文档列表
        :return: 切分后的文本块列表
        """
        chunks = []
        for doc in documents:
            splits = self.text_splitter.create_documents(
                texts=[doc["content"]],
                metadatas=[doc["metadata"]]
            )
            for split in splits:
                chunks.append({
                    "txt": split.page_content,
                    "metadata": split.metadata,
                    "length": len(split.page_content)
                })
        return chunks

    def analyze_chunks(self, chunks: List[Dict]):
        """
        分析切分结果
        """
        avg_len = sum(chunk["length"] for chunk in chunks) / len(chunks)
        print(f"共切分 {len(chunks)} 个文本块")
        print(f"平均长度: {avg_len:.1f} 字符")
        print("\n示例文本块：")
        for i in [0, len(chunks) // 2, -1]:  # 显示首、中、尾三个样本
            print("-" * 50)
            print(f"[块 {i + 1}] {chunks[i]['txt'][:100]}...")
            print(f"来源: 第 {chunks[i]['metadata'].get('page', '?') + 1} 页")


