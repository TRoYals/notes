---
title: Lambda
date: 2023-07-10 09:32
article: false
tag: 
---

Python Lambda 简明记录

<!-- more -->

## 背景知识

为了更深入的了解 Lambda,你需要了解什么是 [[../../../09 Tasks/函数式编程/01|函数式编程]]

### Source

[How to Use Python Lambda Functions – Real Python](https://realpython.com/python-lambda/#lambda-calculus)

## Syntax of lambda
### No Statements

A lambda function can’t contain any statements. In a lambda function, statements like `return`, `pass`, `assert`, or `raise` will raise a [`SyntaxError`](https://realpython.com/invalid-syntax-python/) exception.

### Single Expression

### Type Annotations

不支持 Type Check.

### IIFE
```python

> > > (lambda x: x * x)(3)  
9
```

## Arguments
```python
>>> (lambda x, y, z: x + y + z)(1, 2, 3)
6
>>> (lambda x, y, z=3: x + y + z)(1, 2)
6
>>> (lambda x, y, z=3: x + y + z)(1, y=2)
6
>>> (lambda *args: sum(args))(1,2,3)
6
>>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
6
>>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
6
```
