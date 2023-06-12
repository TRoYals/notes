---
title: Lib ABC
date: 2023-06-07 17:46
article: false
star: false
check: 0
---

## 相关文档
[官方文档](https://docs.python.org/3/library/abc.html)

## 介绍

ABC是Python标准库中的一个模块，全称为Abstract Base Classes（抽象基类），它提供了一组抽象的基类，可以用来定义和检查其他类的接口和行为。

ABC模块的主要作用是帮助开发者定义和实现接口，这些接口可以是抽象的，也可以是具体的。通过继承ABC库中提供的抽象基类，我们可以定义自己的类，并且确保这些类实现了所需的接口和行为。

使用ABC库，可以让代码更加清晰和易于维护。例如，如果我们要定义一个需要实现某些方法的类，我们可以通过继承ABC库中的抽象基类来确保这些方法都被实现了，否则在调用时会抛出异常提示开发者需要实现哪些方法。

总之，ABC库提供了一种规范化的方式来定义和实现接口，可以提高代码的可读性和可维护性。

## Learn By Case
[[../../../源码/LangChain 源码解析|LangChain]]中第一次commit中因为后续需要导入不同的语言模型, 所以定义了一个base模型. 同样的, 在一个udemy的爬虫源码中, 因为后续可以对多个免费的课程库进行信息获取, 作者也定一个了一个抽象基类来供后续人员开发.


#### LangChain 中的abc
```python
"""Base interface for large language models to expose."""
from abc import ABC, abstractmethod
from typing import List, Optional


class LLM(ABC):
    """LLM wrapper should take in a prompt and return a string."""

    @abstractmethod
    def __call__(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """Run the LLM on the given prompt and input."""
```

1. 如何将abc 和[[Lib Pydantic|pydantic]]结合?　
同样是LangChain, 作者是这样做的
```python

from pydantic import BaseModel, Extra, root_validator
from langchain.llms.base import LLM

class OpenAI(BaseModel, LLM):
...
```