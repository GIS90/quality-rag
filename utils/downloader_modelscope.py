# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    ModelScope下载器
    - 下载
    - 上传

base_info:
    __author__ = "PyGo"
    __time__ = "2025/7/4 8:45"
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
# usage: /usr/bin/python downloader_modelscope.py
# ------------------------------------------------------------
import os
from modelscope.hub.snapshot_download import snapshot_download
from modelscope.hub.api import HubApi
from modelscope.hub.constants import Licenses, ModelVisibility
from deploy.utils import hashlib_md5
from deploy.config import MS_ACCESS_TOKEN, MS_USER_NAME, MODEL_CACHE_DIR


# 下载模型
def download_model(model_id, local_dir):
    snapshot_download(model_id=model_id, local_dir=local_dir)
    print(f"模型 {model_id} 下载完成，保存路径: {local_dir}")


# 上传模型到指定用户空间
def upload_model_to_space(model_id, local_cache_dir):
    try:
        api = HubApi()
        api.login(MS_ACCESS_TOKEN)

        # 创建模型库
        api.create_model(
            model_id,
            visibility=ModelVisibility.PUBLIC,  # 模型的可见性,1-私有，5-公开，不填默认5
            license=Licenses.APACHE_V2,
            chinese_name="Qwen3-Embedding-0.6B上传测试0"
        )

        # 上传模型文件夹
        api.upload_folder(
            repo_id=model_id,
            folder_path=local_cache_dir,
            repo_type="model",  # 模型类型, model or dataset
            commit_message='上传Qwen3-Embedding-0.6B模型'
        )
        print(f"模型已成功上传到 {model_id}")
    except Exception as e:
        print(f"上传失败: {str(e)}")


# 配置模型ID
model_id = 'Qwen/Qwen3-8B'
model_local = "%s/%s" % (MODEL_CACHE_DIR, model_id)


# 下载模型
if os.path.exists(model_local):
    print(f"{model_local}模型已存在，退出。。。。。。")
    os._exit(0)

download_model(model_id=model_id, local_dir=model_local)

# 上传模型到指定用户空间
upload_model_name = "Qwen3-Embedding-0.6B-" + hashlib_md5(content=MS_ACCESS_TOKEN)
model_id = f"{MS_USER_NAME}/{upload_model_name}"
# upload_model_to_space(model_id, model_local)
