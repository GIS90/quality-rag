# RAG配置
TOP = 3
CHUNK_SIZE = 200
CHUNK_OVERLAP = 25

# 向量数据库
VECTOR_DB_PATH = "./chroma_db_data"
VECTOR_COLLECTION_NAME = "quality-rag-Q"

# 文档列表，当前只支持[txt md pdf]格式
# 可以设定目录或者具体文件列表
DOCUMENT_LIST = [
    "E:/project-ai/quality-rag/datas/md",
    # "E:/project-ai/quality-rag/datas/pdf",
]

# Modelscope账户
MS_USER_NAME = 'Pygo222'
MS_ACCESS_TOKEN = '4c35372c-ed7b-4fb7-bc8d-74b7bf26b6cb'

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >
# 本地模型配置
MODEL_CACHE_DIR = "D:/AI_MODELS"
MODEL_EMBEDDING = "BAAI/bge-base-en-v1.5"
MODEL_AI = "Qwen/Qwen3-0.6B"

# Ollama模型配置
OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL_ID = "qwen3:8b"

# API模型配置 deepseek
DS_API_KEY = ""
DS_BASE_URL = "https://api.deepseek.com"
DS_MODEL_ID = "deepseek-chat"
# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
