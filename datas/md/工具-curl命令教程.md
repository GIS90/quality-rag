# 😈`curl` 命令使用教程

`curl` 是一个强大的命令行工具，用于在终端中传输数据，支持多种协议（如 HTTP、HTTPS、FTP、SMTP 等）,适用于测试 Web 接口、下载文件、调试服务等场景。它是开发人员调试 API 和下载文件时常用的工具,熟练掌握其常用参数可以显著提升开发效率。

------

## 安装 curl

大多数 Linux 发行版和 macOS 都预装了 `curl`。如果没有安装，可以通过以下方式安装：
### Windows

从 **Windows 10** 和 **Windows 11** 开始，系统已经内置了 `curl` 命令，官网下载：https://curl.se/download.html
下载安装包，手动安装好后，将 curl.exe 添加到系统环境变量 PATH。
```bash
# 查看版本
curl --version
```

### Ubuntu / Debian

```bash
sudo apt update && sudo apt install curl
```

### CentOS / RHEL

```bash
sudo yum install curl
```

### macOS (使用 Homebrew)

```bash
brew install curl
```

------

## 基本用法

### 获取网页内容（默认GET 请求）

```bash
# 语法糖
curl [选项] [URL]
curl http://example.com
```
这会输出请求网页的 HTML 源码到终端。

### 将结果保存到文件

- 使用 `-o` 保存文件并指定名称：

```bash
curl -o index.html http://example.com
```

- 使用 `-O` 保存为远程文件名相同的名字：

```bash
curl -O https://example.com/file.txt 
```

### 发送 POST 请求

```bash
curl -X POST -d "param1=value1&param2=value2" http://example.com/api
```
- `-X POST`：指定请求方法为 POST。
- `-d`：发送的数据体。

### 设置请求头

```bash
curl -H "Content-Type: application/json" \
​     -H "Authorization: Bearer YOUR_TOKEN" \
​     http://api.example.com/data
```
- -H：添加请求头。

### 使用 JSON 数据发送 POST 请求

```bash
curl -X POST \
​     -H "Content-Type: application/json" \
​    -d '{"username":"user1", "password":"pass1"}' \
​     http://api.example.com/login
```

### 使用 Basic Auth 登录

```bash
curl -u username:password http://example.com/secure
```

### 跟随重定向

> 默认情况下，`curl` 不会自动跟随重定向。添加 `-L` 参数来启用：
>

```bash
curl -L http://example.com
```

### 显示详细信息

使用 `-v` 可以查看详细的请求和响应过程（包括 headers）：

```bash
curl -v http://example.com
```

------
## 参数列表

|参数	|作用	|示例|
| :----------------:| :----------------:| :----------------:|
|-X	|指定 HTTP 方法	|curl -X DELETE https://api.example.com/item/123|
|-H|	添加请求头|	|curl -H "Authorization: Bearer token" https://api.example.com|
|-d	|发送请求体数据	|curl -d "param1=value1" https://example.com|
|-o|	输出到文件	|curl -o download.zip https://example.com/file.zip|
|-L	|跟随重定向	|curl -L https://short.url|
|-k	|跳过 SSL 验证（不安全）|	curl -k https://self-signed.badssl.com|
|-u	|基本认证	|curl -u username:password https://api.example.com|


## 示例合集

| 功能             | 命令                                                         |
| :------------------------------: | :---------------------------------------------- |
|  获取网页内容  |`curl https://example.com`  |
| 下载文件         | `curl -O https://example.com/file.zip`          |
| 发送 JSON 到 API | `curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://api.example.com` |
| 登录认证请求     | `curl -u username:password https://api.example.com`           |
| 获取 HTTP 状态码 | `curl -I http://example.com`           |
| 跟随重定向  | `curl -L http://example.com`  |

------

## 📚 参考资料

- [curl 官方网站](https://curl.se/)
- [curl 命令手册](https://curl.se/docs/manpage.html)

