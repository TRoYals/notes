---
title: 02pathlib
date: 2023-06-25 10:17
article: false
tags:
---

## 介绍

提供了一种<font color="#f79646">面向对象</font>的路径管理模式  
为什么使用 Pathlib 而不是 os.path

1. 老的路径操作函数管理比较混乱，有的是导入 os, 有的又是在 os.path 当中，而新的用法统一可以用 pathlib 管理。
2. 老用法在处理不同操作系统 win，mac 以及 linux 之间很吃力。换了操作系统常常要改代码，还经常需要进行一些额外操作。
3. 老用法主要是函数形式，返回的数据类型通常是字符串。但是路径和字符串并不等价，所以在使用 os 操作路径的时候常常还要引入其他类库协助操作。新用法是面向对象，处理起来更灵活方便。
4. pathlib 简化了很多操作，用起来更轻松。

资源文档:

- [pathlib --- 面向对象的文件系统路径 — Python 3.11.4 文档](https://docs.python.org/zh-cn/3/library/pathlib.html)
- [<font color="#f79646">python 路径操作新标准：pathlib 模块 - 知乎</font>](https://zhuanlan.zhihu.com/p/139783331)
- [pathlib库，文件与文件夹处理的 "四大天王" 之一，贼好用！](https://mp.weixin.qq.com/s/upXCeqRAsR-dZdr_UPwLvA)

如果以前从未用过此模块，或不确定哪个类适合完成任务，那要用的可能就是 **Path**。它在运行代码的平台上实例化为 具体路径。

![image.png](http://oss.naglfar28.com/naglfar28/202306251125197.png)

## 基础使用

列出子目录

```python
   from pathlib import Path
   p = Path('.')
   [x for x in p.iterdir() if x.is_dir()]
```

列出所有.py 文件

```python
 p = Path('.')
[x for x in p.iterdir() if x.is_file() and x.suffix == '.py']#方法1
list(p.glob('**/*.py'))#方法2
```

在目录树中移动

```python
p = Path('/etc')
q = p / 'init.d' / 'reboot'
q
#PosixPath('/etc/init.d/reboot')
q.resolve()
#PosixPath('/etc/rc.d/init.d/halt')
```

查询路径的属性

```python
q.exists()
#True
q.is_dir()
#False
path.is_file()  # True if path is a regular file
path.is_symlink()
```

打开文件

```python
with q.open() as f: f.readline()

```

- 获取文件属性

文件属性比如文件大小，创建时间，修改时间等等。

```text
file = Path('archive/demo.txt')
print(file.stat())
print(file.stat().st_size)
print(file.stat().st_atime)
print(file.stat().st_ctime)
print(file.stat().st_mtime)
```

找出最后修改的文件的例子：

```text
>>> path = Path.cwd()
>>> max(
        [(f.stat().st_mtime, f) 
         for f in path.iterdir() 
         if f.is_file()]
    )
1589171135.860173 C:\Users\me\study\demo_03.py
```
