# Quality-Rag

基于Python语言，结合Langchain、第三方AI接口搭建开发的RAG简单问答系统，用***uv***命令管理运行环境，加入了streamlit生成简单的rag页面。

## 架构
- 开发语言：Python语言
- 向量数据库：Chromadb
- 切词：Langchain
- 语言模型：HuggingFace本地大模型、Deepseek API
- RAG框架：Llama-Index

## 项目结构

- app
  * app_by_api.py：rag运行调用第三方API
  * app_by_llm.py：用本地模型运行rag
- deploy
  * spliter.py：文档切词工具
  * vector.py：向量数据库模型
  * ai.py：AI语言模型配置，配置了RAGHuggingFaceAI（本地模型）、RAGOllamaAI（本地Ollama）、RAGDeepseekAI（Deepseek第三方API）  
    因为本地运行大模型太慢了，所以后期改为使用Deepseek第三方API
  * config.py：配置文件，包含RAG配置、模型配置、文档配置等内容，具体查看文件；其中重要的API-KEY配置在.env文件中
- utils
  * document_vectorization.py：文档向量化，加载到向量数据库，在config.py配置了文件目录/文件列表
  * downloader_huggingface.py：HuggingFace大模型下载器
  * downloader_modelscope.py：Modelscope大模型下载器


## 部署
第一步：配置环境变量deploy/config.py  
第二步：uv构建运行环境  
第三步：启动服务streamlit run app_by_api.py  

## 结束语
当今快速发展的世界，唯有自我学习成长，才能保持不被淘汰。