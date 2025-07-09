# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    工具集

base_info:
    __author__ = "PyGo"
    __time__ = "2025/7/4 8:32"
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
# usage: /usr/bin/python utils.py
# ------------------------------------------------------------
import os
import hashlib
from datetime import datetime
from deploy.config import VECTOR_DB_PATH, MODEL_EMBEDDING, MODEL_AI, MODEL_CACHE_DIR


def get_root_path() -> str:
    """
    项目根目录
    :return: abs path
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_vector_abs_path() -> str:
    """
    向量数据库的绝对路径
    :return: abs path
    """
    return os.path.join(get_root_path(), VECTOR_DB_PATH)


def get_dotenv() -> str:
    """
    .env文件
    :return:
    """
    return os.path.join(get_root_path(), '.env')


def hashlib_md5(content: str, length: int =8):
    """
    hashlib md5加密
    """
    _c = content + datetime.now().strftime("%Y%m%d%H%M%S")
    return hashlib.md5(_c.encode()).hexdigest()[:length]


def get_model_embedding() -> str:
    """
    embedding model
    :return:
    """
    return f"{MODEL_CACHE_DIR}/{MODEL_EMBEDDING}"


def get_model_ai() -> str:
    """
    ai model
    :return:
    """
    return f"{MODEL_CACHE_DIR}/{MODEL_AI}"

