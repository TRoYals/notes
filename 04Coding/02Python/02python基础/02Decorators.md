---
title: Decorators
date: 2023-07-10 10:04
article: false
tag:
---

<!-- more -->

## 背景

## 相关知识

[[../../../09Tasks/函数式编程/01|函数式编程]]

### Source

[PEP 318 – Decorators for Functions and Methods | peps.python.org](https://peps.python.org/pep-0318/)

## 什么是 Decorators

在 Python 中，装饰器（Decorators）是一种特殊的语法构造，用于修改或扩展函数或类的行为。装饰器允许我们在不修改原始函数或类定义的情况下，通过在其周围添加额外的逻辑或功能来改变它们的行为。

装饰器实际上是一个高阶函数，它接受一个函数或类作为输入，并返回一个经过修改的函数或类。装饰器可以在不影响原始函数或类的代码的情况下，对其进行包装、修改或扩展。

装饰器的常见用途包括：

1. 添加日志记录：装饰器可以用于在函数执行前后记录日志信息，以便调试或跟踪函数的执行。
2. 计时函数执行时间：装饰器可以用于计时函数的执行时间，以便了解函数的性能。
3. 权限检查：装饰器可以用于检查用户的权限或角色，并根据结果决定是否执行函数。
4. 缓存结果：装饰器可以用于缓存函数的结果，以提高性能和避免重复计算。
5. 类注册和扩展：装饰器可以用于注册类或在类定义时扩展其功能。

下面是一个示例，演示了装饰器的使用：

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function", func.__name__, "finished execution")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

result = add(3, 5)
print("Result:", result)
"""output
Calling function: add
Function add finished execution
Result: 8
"""
```

在上述示例中，我们定义了一个名为 `logger` 的装饰器函数，它接受一个函数作为参数，并返回一个包装函数 `wrapper`。在 `wrapper` 函数中，我们添加了额外的日志记录逻辑。通过在 `add` 函数定义前添加 `@logger` 装饰器，我们将 `add` 函数传递给 `logger` 装饰器进行包装。当我们调用 `add` 函数时，实际上是调用了经过装饰器修改后的 `wrapper` 函数，从而实现了日志记录的功能。

总之，装饰器是一种强大的语法构造，用于修改或扩展函数或类的行为。它们使得我们可以在不修改原始代码的情况下，通过添加额外的逻辑或功能来改变函数或类的行为。
