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

HuggingFace
-----------------------------------------------------------------------------------------------------------------------
1、核心参数
>>>>>>>>>>>>>>>>>
参数名	            类型	    必选	    默认值	    说明
model_name	        str	    ✅	    -	        HuggingFace 或 ModelScope 的模型 ID（如 "Qwen/Qwen-1_8B"）
tokenizer_name	    str	    ❌	    model_name	分词器名称（默认与 model_name 相同）
device_map	        str	    ❌	    "auto"	    设备分配策略（"auto", "cuda", "cpu"）
model_kwargs	    Dict	❌	    {}	        传递给 AutoModel.from_pretrained() 的参数字典（如 {"trust_remote_code": True}）
tokenizer_kwargs	Dict	❌	    {}	        传递给 AutoTokenizer.from_pretrained() 的参数字典
generate_kwargs	    Dict	❌	    {}	        生成文本时的参数（如 {"max_length": 512, "temperature": 0.7}）
-----------------------------------------------------------------------------------------------------------------------
2、高级参数
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


Ollama
-----------------------------------------------------------------------------------------------------------------------
1. 核心参数（必填）
>>>>>>>>>>>>>>>>>
参数名	    类型	    默认值	                    说明
model	    str	    -	                        Ollama 模型名称（如 "llama3", "mistral", "phi3" 等）。必须显式指定。
base_url	str	    "http://localhost:11434"	Ollama 服务的 URL（若 Ollama 运行在其他地址或端口，需修改）。
-----------------------------------------------------------------------------------------------------------------------
2、模型生成参数（控制输出行为）
>>>>>>>>>>>>>>>>>
参数名	        类型	        默认值	说明
temperature	    float	    0.8	    控制随机性（0.0-1.0）。值越低，输出越确定；值越高，越有创造性。
top_p	        float	    0.9	    Nucleus 采样阈值（0.0-1.0）。仅保留概率质量超过阈值的 token。
top_k	        int	        40	    限制每一步生成的候选 token 数量。
num_ctx	        int	        2048	上下文窗口大小（token 数）。
num_predict	    int	        128	    生成的最大 token 数。
stop	        List[str]	None	遇到指定字符串时停止生成（如 ["\n", "###"]）。
seed	        int	        None	随机种子（固定种子可复现结果）。
-----------------------------------------------------------------------------------------------------------------------
3、请求控制参数
>>>>>>>>>>>>>>>>>
参数名	            类型	            默认值	说明
request_timeout	    float	        60.0	请求超时时间（秒）。
headers	            Dict[str, str]	None	自定义 HTTP 请求头（如认证头）。
-----------------------------------------------------------------------------------------------------------------------
4、高级参数
>>>>>>>>>>>>>>>>>
参数名	        类型	    默认值	说明
keep_alive	    str	    "5m"	控制模型在 Ollama 内存中的保留时间（如 "10m", "1h"）。设为 "-1" 表示永久保留。
tfs_z	        float	None	Tail-free 采样参数（减少低概率 token 的影响）。
mirostat	    int	    None	启用 Mirostat 采样（1 或 2）。
-----------------------------------------------------------------------------------------------------------------------

Deepseek:
    def test():
        print("* " * 22+"start")
        ai = RAGDeepseekAI()
        # 模型列表
        print(ai.get_model_list())
        # 用户余额
        print(ai.get_user_balance())

        # 对话
        print(ai.chat(content="介绍下自己"))
        print("* " * 22 + "end")

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
# usage: /usr/bin/python ai.py
# ------------------------------------------------------------
import json
import requests
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.llms.ollama import Ollama
from transformers import AutoTokenizer, AutoModelForCausalLM

from deploy.utils import get_model_ai
from deploy.config import (OLLAMA_MODEL_ID, OLLAMA_URL,
                           DS_MODEL_ID, DS_BASE_URL, DS_API_KEY)

__all__ = [
    "RAGHuggingFaceAI",
    "RAGOllamaAI",
    "RAGDeepseekAI",
]

MODEL_AI = get_model_ai()

tokenizer = AutoTokenizer.from_pretrained(MODEL_AI)
model = AutoModelForCausalLM.from_pretrained(MODEL_AI)

system_prompt = """你是一个RAG系统助手，专门帮助用户基于给定的上下文内容回答问题，严格根据提供的检索内容回答问题。
- 仅使用检索到的信息生成回答，禁止编造未知内容。
- 如果检索结果不包含答案，回复：“未找到相关信息。
- 回答应简洁明了，不添加额外解释或发挥。
- 请严格按照用户的指示进行判断和回答，不得使用自己的知识库或常识来回答问题。
"""


class RAGHuggingFaceAI:
    """
    RAG HuggingFace AI
    """

    def __init__(self):
        self.llm = HuggingFaceLLM(
            model=model,
            tokenizer=tokenizer,
            device_map="auto",
            context_window=2048,
            max_new_tokens=256,
            system_prompt=system_prompt,
            generate_kwargs={"temperature": 0.1},
        )


class RAGOllamaAI:
    """
    RAG Ollama AI
    """

    def __init__(self):
        self.llm = Ollama(
            model=OLLAMA_MODEL_ID,
            base_url=OLLAMA_URL,
            temperature=0.1,
            top_p=0.9,
            request_timeout=60.0,
        )


class RAGDeepseekAI:
    """
    RAG Deepseek AI
    """

    def __init__(self):
        """
        初始化，配置相关API_KEY、Model、URL
        """
        self.key = DS_API_KEY
        self.model = DS_MODEL_ID
        self.base_url = DS_BASE_URL
        self.__HEADERS = {
            "Accept": "application/json",
            "Authorization": "Bearer %s" % DS_API_KEY
        }

    def get_model_list(self) -> list:
        """
        模型列表
        """
        url = f"{self.base_url}/models"
        payload = {}
        headers = {"api": "/models"}
        headers |= self.__HEADERS
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json().get("data")

    def get_user_balance(self) -> dict:
        """
        用户余额
        """
        url = f"{self.base_url}/user/balance"
        payload = {}
        headers = {"api": "/user/balance"}
        headers |= self.__HEADERS
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()

    def chat(self, content: str) -> str:
        url = f"{self.base_url}/chat/completions"
        payload = json.dumps({
          "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content}
          ],
          "model": self.model,
          "frequency_penalty": 0,
          "max_tokens": 2048,
          "presence_penalty": 0,
          "response_format": {
            "type": "text"
          },
          "stop": None,
          "stream": False,
          "stream_options": None,
          "temperature": 0.1,
          "top_p": 1,
          "tools": None,
          "tool_choice": "none",
          "logprobs": False,
          "top_logprobs": None
        })
        headers = {
          "api": "/chat/completions",
          'Content-Type': 'application/json',
        }
        headers |= self.__HEADERS
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()["choices"][0]["message"]["content"]


