# 🚀uv命令教程 —— Python 包管理新体验

***uv***是一个由 Rust 编写的高性能 Python 包管理工具，旨在替代 `pip`、`virtualenv` 和 `pip-tools`，速度提升 10-100 倍。它不仅速度快，还内置了虚拟环境管理和依赖解析功能，是现代 Python 开发的新选择。

## 安装 `uv`  

### 安装方式有很多，这里列举最常用的 2 种。

```bash
pip install uv
或者
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> ✅ 确保你已安装 Python 并配置好环境变量。 

### 配置国内镜像加速

```
# 临时使用清华源
export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

# 永久配置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"' >> ~/.zshrc
```

------

## 核心命令一览

### 初始化项目

| 功能                                 | 命令示例                |
| :----------------------------------- | :---------------------- |
| 初始化项目（项目文件夹已存在）       | `cd XXXX && uv init`    |
| 初始化并创建项目（项目文件夹不存在） | `uv init my-uv-project` |

初始化项目之后会生成 pyproject.toml、.gitignore、README.md 等文件，pyproject.toml 主要是项目的基本信息，比如 requires-python、dependencies 等等。

### 创建虚拟环境

| 功能                        | 命令示例                    |
| :-------------------------- | :-------------------------- |
| 创建虚拟环境                | `uv venv`                   |
| 自定义路径创建              | `uv venv myenv`             |
| 创建环境并指定 Python 版本  | `uv venv -p 3.11 myenv`     |
| 删除环境                    | `uv venv --remove .venv`    |
| 激活虚拟环境（Linux/macOS） | `source .venv/bin/activate` |
| 激活虚拟环境（Windows）     | `.venv\Scripts\activate`    |

### python 版本管理

| 功能                                  | 命令示例                   |
| :------------------------------------ | :------------------------- |
| 列举 python 列表                        | `uv python list`           |
| 安装指定版本                          | `uv python install 3.12`   |
| 项目使用指定版本并更新.python-version | `uv python pin 3.12`       |
| 卸载指定版本                          | `uv python uninstall 3.12` |

### 包管理

| 功能                          | 命令示例                             |
| :---------------------------- | :----------------------------------- |
| 安装单个包                    | `uv pip install requests`            |
| 安装多个包                    | `uv pip install numpy pandas flask`  |
| 安装所有依赖                  | `uv pip install -r requirements.txt` |
| 冻结当前环境依赖              | `uv pip freeze > requirements.txt`   |
| 卸载包                        | `uv pip uninstall requests`          |
| 查看已安装包                  | `uv pip list`                        |
| 升级包                        | `uv pip install --upgrade requests`  |
| 安装依赖并更新 pyproject.toml | `uv add 包名1 包名2 包名N `          |
| 移动依赖并更新 pyproject.toml | `uv remove 包名`                     |
| 同步依赖（非常好用）          | `uv sync`                            |
| 生成/更新锁定文件             | `uv lock`                            |
| 列举项目包结构                | `uv tree`                            |

### 运行项目

| 功能 | 命令示例         |
| :--- | :--------------- |
| 运行 | `uv run main.py` |

项目如果没有进行虚拟环境创建，会自动依据 pyproject.toml 文件配置的 python 版本自动创建.venv 虚拟环境，使用创建的 python 运行项目。

### 打包&&发布

| 功能 | 命令示例     |
| :--- | :----------- |
| 打包 | `uv build`   |
| 发布 | `uv publish` |

以上就是 ***UV*** 常用的基本命令，如果项目详细了解更多的内容，请查看 `uv --help`。

------

## 快速开始项目流程示例

```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# 安装依赖
uv pip install flask

# 安装所有依赖项
uv pip install -r requirements.txt

# 冻结依赖
uv pip freeze > requirements.txt

# 卸载不需要的包
uv pip uninstall flask
```

------

## 自动清理和修复依赖（实验性）

```bash
uv pip check
```

未来版本将支持更强大的依赖管理功能，包括依赖锁定和同步。

------

## 配置与集成建议

你可以在项目根目录下创建 `pyproject.toml` 来配置 `uv` 的行为（目前部分功能还在开发中）。

------

## uv 与其他工具对比

| 特性         | uv             | pip            | virtualenv |
| ------------ | :--------------: | :--------------: | :----------: |
| 安装速度     | ⚡ 极快（Rust） | 中等           | 慢         |
| 虚拟环境支持 | ✅ 内置         | ❌              | ✅          |
| 依赖解析     | ✅ 内置高效     | 基础支持       | ❌          |
| 锁文件支持   | ✅ soon         | 需要 pip-tools | ❌          |
| 兼容性       | ✅ pip 兼容     | 原生支持       | 原生支持   |

总之一句话，***uv 牛逼就对了***。

------

## 📚参考资料

- GitHub: https://github.com/astral-sh/uv
- 官方文档: https://docs.astral.sh/uv/