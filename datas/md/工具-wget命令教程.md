# 🏎️wget命令使用教程

`wget` 【下载神器，功能是缩小版本的迅雷】是一个非常强大且常用的命令行工具，用于从网络上下载文件。它支持 HTTP、HTTPS 和 FTP 协议，并具备断点续传、后台下载等功能。

------

## 🧰 安装 wget（如未预装）

大多数 Linux 发行版默认已安装 `wget`，如果没有，请根据你的系统进行安装：

- **Windows**
```
下载地址：https://sourceforge.net/projects/gnuwin32/files/wget/
选择对应的版本，进行.exe安装。
```

- **Debian/Ubuntu** :

```bash
sudo apt update && sudo apt install wget
```

- **CentOS/RHEL** :

```bash
sudo yum install wget
```

- **macOS (使用 Homebrew)** :

```bash
brew install wget
```

------

## 基本用法

### 下载单个文件

```bash
wget https://example.com/file.zip 
```
这会将文件下载到当前目录，并保留原始文件名。

### 指定保存的文件名

使用 `-O` 参数指定下载后保存的文件名：

```bash
wget -O myfile.zip http://example.com/file.zip
```

### 断点续传（继续下载）

如果下载中断，可以用 `-c` 参数继续下载：
```bash
wget -c http://example.com/largefile.iso
```

### 后台下载

使用 `-b` 参数在后台运行：

```bash
wget -b http://example.com/file.zip
```
日志会写入 `wget-log` 文件中。

### 设置下载重试次数

使用 `-t` 指定最大尝试次数：

```bash
wget -t 5 http://example.com/file.zip
```

### 限制下载速度

防止占用全部带宽，可使用 `--limit-rate`：

```bash
wget --limit-rate=100k http://example.com/file.zip
```
单位可以是 `k`（千字节）或 `m`（兆字节）。

### 超时设置

配置下载请求超时的时间，单位是：秒

```bash
wget --timeout=30 https://example.com
```

### 镜像整个网站（用于备份）

```bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent http://example.com
```

说明：
- `--mirror`: 开启镜像模式（等同于 `-r -N`）
- `--convert-links`: 转换链接以便本地查看
- `--adjust-extension`: 添加合适的扩展名
- `--page-requisites`: 下载页面所需资源（如图片、CSS）
- `--no-parent`: 不访问父目录

### 递归下载某个目录下的所有文件

```bash
wget -r http://example.com/files/
```

### 使用用户名和密码下载

适用于需要认证的 FTP 或网页：

```bash
wget --user=username --password=password http://example.com/secret/file.zip
```
> ⚠️ 注意：出于安全考虑，建议使用 `--input-file` 或脚本方式避免明文密码出现在历史记录中。 


### 从文件列表批量下载

创建一个包含 URL 的文本文件（每行一个）：

```bash
http://example.com/file1.zip
http://example.com/file2.zip
```

然后使用 `-i` 参数进行批量下载：

```bash
wget -i urls.txt
```

## 其他实用选项

| 选项                | 说明                             |
| ------------------- | -------------------------------- |
| `-q`                | 静默模式（不输出信息）           |
| `-v`                | 显示详细信息（默认）             |
| `-S`                | 显示服务器响应头                 |
| `--timeout=seconds` | 设置连接超时时间                 |
| `-A`                | 指定允许下载的文件类型（白名单） |
| `-R`                | 指定禁止下载的文件类型（黑名单） |

------


## 总结

| 功能       | 命令                      |
| ---------- | ------------------------- |
| 下载文件   | `wget [URL]`              |
| 指定文件名 | `wget -O filename [URL]`  |
| 断点续传   | `wget -c [URL]`           |
| 后台下载   | `wget -b [URL]`           |
| 批量下载   | `wget -i file.txt`        |
| 镜像网站   | `wget --mirror ... [URL]` |

------

## 常见问题

### Q: 如何查看 `wget` 版本？

```bash
wget --version
```

### Q: 如何只下载网页中的图片？

```bash
wget -r -A.jpg,.png http://example.com
```

### Q: 证书错误（--no-check-certificate）
```bash
wget --no-check-certificate https://self-signed.example.com
```

### Q: 处理重定向（--max-redirect）

限制最多 5 次重定向
```bash
wget --max-redirect=5 https://example.com
```

### Q: 解决 403 禁止访问（--user-agent）
```bash
wget --user-agent="Mozilla/5.0" https://example.com
```
------

## 📚参考资料

- 官方主页：https://www.gnu.org/software/wget/
- 官方文档：https://www.gnu.org/software/wget/manual/wget.html
 - Windows 版本下载：https://sourceforge.net/projects/gnuwin32/files/wget/

