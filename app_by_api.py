# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    app run by api

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
import streamlit as st
from deploy.vector import VectorChromaDB
from deploy.config import VECTOR_COLLECTION_NAME, TOP
from deploy.utils import get_vector_abs_path
from deploy.ai import RAGDeepseekAI


# 向量数据库
vector = VectorChromaDB(
    path=get_vector_abs_path(),
    collection_name=VECTOR_COLLECTION_NAME
)
# AI>Deepseek
ai = RAGDeepseekAI()

# ------------------------------
# web
# ------------------------------
st.title("📖 质量大Q智能问答RAG系统")
st.markdown("基于检索增强生成（RAG）的问答工具，无需上传文件，直接提问即可！")
st.text("请输入你的问题（回车/提交）：")
col1, col2 = st.columns([4, 1])  # 第一列宽度占4/5，第二列占1/5
with col1:
    question = st.text_input(
        label="问题：",
        label_visibility="collapsed",
        placeholder="例如：wget命令可以做什么？"
    )
with col2:
    submit_button = st.button("提交")

if question or (question and submit_button):
    print('>'*55 + 'start')
    contents = vector.query(query_texts=question, top=TOP)
    line_contents = "文档检索内容：\n"
    for doc in contents:
        if not doc: continue
        line_contents += "第%d段内容：%s；\n" % (doc.get("top"), doc.get("txt"))
    line_contents += "问题：%s，请基于上述文档检索内容给出正确的答案" % question
    response = ai.chat(line_contents)
    print(f"问题: {question}")
    print(f"回答: {response}")
    print('<'*55 + 'end')

    # 显示答案
    st.subheader("回答：")
    st.text(response)


