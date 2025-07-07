# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    RAG AI

base_info:
    __author__ = "PyGo"
    __time__ = "2025/7/7 15:06"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "quality-rag"

usage:
-----------------------------------------------------------------------------------------------------------------------
核心参数
>>>>>>>>>>>>>>>>>
参数名	            类型	    必选	    默认值	    说明
model_name	        str	    ✅	    -	        HuggingFace 或 ModelScope 的模型 ID（如 "Qwen/Qwen-1_8B"）
tokenizer_name	    str	    ❌	    model_name	分词器名称（默认与 model_name 相同）
device_map	        str	    ❌	    "auto"	    设备分配策略（"auto", "cuda", "cpu"）
model_kwargs	    Dict	❌	    {}	        传递给 AutoModel.from_pretrained() 的参数字典（如 {"trust_remote_code": True}）
tokenizer_kwargs	Dict	❌	    {}	        传递给 AutoTokenizer.from_pretrained() 的参数字典
generate_kwargs	    Dict	❌	    {}	        生成文本时的参数（如 {"max_length": 512, "temperature": 0.7}）
-----------------------------------------------------------------------------------------------------------------------
高级参数
>>>>>>>>>>>>>>>>>
参数名	                类型	                说明
context_window	        int	                模型的最大上下文窗口（默认根据模型自动推断）
max_new_tokens	        int	                生成的最大 token 数（覆盖 generate_kwargs 中的设置）
is_chat_model	        bool	            是否为对话模型（如 Qwen-Chat，默认自动检测）
callback_manager	    CallbackManager	    回调管理器（用于日志/事件处理）
system_prompt	        str	                系统提示词（对话模型适用）
messages_to_prompt	    Callable	        自定义如何将消息列表转换为 prompt 的函数
completion_to_prompt	Callable	        自定义如何将单条文本转换为 prompt 的函数
-----------------------------------------------------------------------------------------------------------------------

design:

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python ai.py
# ------------------------------------------------------------
from llama_index.llms.huggingface import HuggingFaceLLM
from transformers import AutoTokenizer, AutoModelForCausalLM

from deploy.utils import get_model_ai


__all__ = [
    "RAGHuggingFaceAI",
]


MODEL_AI = get_model_ai()

tokenizer = AutoTokenizer.from_pretrained(MODEL_AI)
model = AutoModelForCausalLM.from_pretrained(MODEL_AI)


class RAGHuggingFaceAI:
    """
    RAG HuggingFace AI
    """
    prompt = """你是一个RAG系统助手，严格根据提供的检索内容回答问题。
        - 仅使用检索到的信息生成回答，禁止编造未知内容。
        - 如果检索结果不包含答案，回复：“未找到相关信息”。
        - 回答需标注引用来源（如“根据文档1提到：...”）。
    """

    def __init__(self):
        self.llm = HuggingFaceLLM(
            model=model,
            tokenizer=tokenizer,
            device_map="auto",
            context_window=2048,
            max_new_tokens=256,
            system_prompt=self.prompt,
            generate_kwargs={"temperature": 0.1},
        )
