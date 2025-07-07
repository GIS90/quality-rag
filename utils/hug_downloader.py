# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    HuggingFace模型下载器

base_info:
    __author__ = "PyGo"
    __time__ = "2025/7/3 22:14"
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
import os.path

# ------------------------------------------------------------
# usage: /usr/bin/python hug_downloader.py
# ------------------------------------------------------------
import os
from huggingface_hub import snapshot_download
from deploy.config import MODEL_CACHE_DIR


"""
embedding模型
 - BAAI/bge-base-en-v1.5
 - BAAI/bge-small-en-v1.5
"""
model_id = "BAAI/bge-small-en-v1.5"


# 本地缓存路径
model_local = "%s/%s" % (MODEL_CACHE_DIR, model_id)


def download_model():
    snapshot_download(
        repo_id=model_id,
        local_dir=model_local,
        local_dir_use_symlinks=False
    )


if os.path.exists(model_local):
    print(f"{model_local}模型已存在，退出。。。。。。")
    os._exit(0)

download_model()
print(f"{model_local}模型下载完成")
