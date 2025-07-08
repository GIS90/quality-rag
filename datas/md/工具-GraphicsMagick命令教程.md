# 💘GraphicsMagick图片处理命令

**GraphicsMagick**被誉为“图像处理的瑞士军刀”，是一个强大、稳定且高效的命令行图像处理工具。它是基于ImageMagick 的分支，提供更高效、稳定的图像处理能力，支持多种图像格式（如 JPG、PNG、GIF、TIFF 等），能够进行图像转换、编辑、合成等操作，无论是简单的图像格式转换，还是复杂的图像特效制作，GM都能轻松解决。 

## 安装

### Linux (Ubuntu/Debian)

```bash
sudo apt-get install graphicsmagick
```

### MacOS (Homebrew)

```bash
brew install graphicsmagick
```

### Windows

前往官网下载安装包：https://sourceforge.net/projects/graphicsmagick/files/graphicsmagick-binaries/1.3.45/
直接找到适配电脑版本的.exe包进行安装。

安装完成后，在终端中输入 `gm` 查看是否安装成功：

```bash
gm --version

# 输出信息
GraphicsMagick 1.3.45 2024-08-27 Q16 http://www.GraphicsMagick.org/
Copyright (C) 2002-2024 GraphicsMagick Group.
Additional copyrights and licenses apply to this software.
See http://www.GraphicsMagick.org/www/Copyright.html for details.
```

------

## 核心命令结果

`gm -help`命令查看，GraphicsMagick的命令参数是一个-，这个要注意，一般的命令参数都是两个--。

|命令|	说明|
|:-----:| :--------|
|convert	|图像格式转换与处理|
|mogrify	|批量处理（直接修改原文件）|
|composite	|图像合成（如水印）|
|identify	|获取图像信息|
|montage	|创建图像拼贴|
|batch |以交互或批处理模式发出多个命令|
|compare |比较两个图像|

------

## 基本命令用法

### 显示图像信息

```bash
gm identify image.jpg
```

如果更加详细信息添加-verbose参数.

### 转换图像格式

将 `image.jpg` 转换为 PNG 格式：

```bash
gm convert image.jpg image.png

# webp格式转换
gm convert image.webp image.png
```

### 调整图像大小

```bash
# 按宽度等比缩放
gm convert input.jpg -resize 800 output.jpg

# 强制尺寸（可能变形）
gm convert input.jpg -resize 800x600! output.jpg

# 填充后裁剪
gm convert input.jpg -resize 800x600^ -gravity center -extent 800x600 output.jpg
```
> `800x600` 表示目标宽度和高度。 

### 裁剪图像

```bash
gm convert input.jpg -crop 100x100+10+20 output.jpg
```
- `100x100`：裁剪区域大小
- `+10+20`：从坐标 (10, 20) 开始裁剪

### 添加水印 / 合成图像

```bash
gm composite -geometry +10+10 watermark.png background.jpg output.jpg
```

### 质量优化

```bash
# 调整 JPEG 质量（1-100）
gm convert input.jpg -quality 85 optimized.jpg

# 减少 PNG 颜色数
gm convert input.png -colors 64 output.png

# 去除 EXIF 信息
gm convert input.jpg -strip output.jpg
```

### 批量处理图像

使用 shell 命令批量调整所有 `.jpg` 图像大小：
```bash
for file in *.jpg; do
    gm convert "$file" -resize 50% "resized_$file"
done

或者

find ./images -name "*.jpg" -exec gm convert {} -resize 1200x {} \;
```

------

## 进阶技巧

### 调整亮度和对比度

```bash
gm convert input.jpg -brightness-contrast 20x10 output.jpg
```
- `20`：增加亮度
- `10`：增加对比度

### 旋转图像

```bash
gm convert input.jpg -rotate 90 output.jpg
```

### 高斯模糊图像

```bash
gm convert input.jpg -blur 0x8 output.jpg
```
- `0x8`：模糊程度，值越大越模糊
### 灰度画图像

```bash
gm convert input.jpg -colorspace GRAY output.jpg
```

### 图像添加边框

```bash
gm convert input.jpg -bordercolor black -border 10x10 output.jpg
```

### 使用管道进行链式操作

```bash
gm convert input.jpg -resize 50% -blur 0x5 -brightness-contrast 10x5 output.jpg
```

------

## 高级功能

### 合并多个图片
```bash
# 水平合并
gm convert +append image1.jpg image2.jpg image3.jpg merged_image.jpg

# 垂直合并
gm convert -append image1.jpg image2.jpg image3.jpg merged_image.jpg
```


### PDF文件处理
```bash
# JPG 转 PDF
gm convert *.jpg combined.pdf

# PDF 转 JPG（多页处理）
gm convert -density 150 document.pdf[0] page1.jpg  # 第一页
gm convert -density 150 document.pdf page%d.jpg    # 所有页
```
pdf转图片需要安装Ghostscript库。

### 动画 GIF 制作

```bash
# 创建 1 秒延迟的 GIF
gm convert -delay 100 frame*.jpg animation.gif

# 优化 GIF 大小
gm convert animation.gif -layers Optimize optimized.gif
```

其中，`-delay 20` 设置每帧之间的延时（单位：1/100秒）。

### 多线程工作

```bash
# 使用 4 个线程
gm convert -threads 4 bigimage.tif output.jpg
```

### 修复损坏图像
```bash
gm convert -regard-warnings input.jpg output.jpg
```
并不是所有的图像都可以修复成果。

------

##  常用图像格式支持

| 格式 | 描述                           |
| :----: | :------------------------------ |
| JPEG | 高压缩有损图像格式             |
| PNG  | 无损压缩，支持透明             |
| GIF  | 支持动画和透明                 |
| BMP  | Windows 位图                   |
| TIFF | 高质量图像，常用于印刷         |
| SVG  | 可缩放矢量图形（需编译时启用） |

------

## 📝参考文档

- 官方网站：http://www.graphicsmagick.org/
- 命令行手册：http://www.graphicsmagick.org/GraphicsMagick.html
