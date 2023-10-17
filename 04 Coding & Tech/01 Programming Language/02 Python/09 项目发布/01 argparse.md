---
title: argparses
date: 2023-07-27 15:30
article: true
tags: 
---

命令行交互的核心

<!-- more -->

## 相关文档

[argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html)

## Argparse

|Name|Description|Values|
|---|---|---|
|[action](https://docs.python.org/3/library/argparse.html#action)|Specify how an argument should be handled|`'store'`, `'store_const'`, `'store_true'`, `'append'`, `'append_const'`, `'count'`, `'help'`, `'version'`|
|[choices](https://docs.python.org/3/library/argparse.html#choices)|Limit values to a specific set of choices|`['foo', 'bar']`, `range(1, 10)`, or [`Container`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container "collections.abc.Container") instance|
|[const](https://docs.python.org/3/library/argparse.html#const)|Store a constant value||
|[default](https://docs.python.org/3/library/argparse.html#default)|Default value used when an argument is not provided|Defaults to `None`|
|[dest](https://docs.python.org/3/library/argparse.html#dest)|Specify the attribute name used in the result namespace||
|[help](https://docs.python.org/3/library/argparse.html#help)|Help message for an argument||
|[metavar](https://docs.python.org/3/library/argparse.html#metavar)|Alternate display name for the argument as shown in help||
|[nargs](https://docs.python.org/3/library/argparse.html#nargs)|Number of times the argument can be used|[`int`](https://docs.python.org/3/library/functions.html#int "int"), `'?'`, `'*'`, or `'+'`|
|[required](https://docs.python.org/3/library/argparse.html#required)|Indicate whether an argument is required or optional|`True` or `False`|
|[type](https://docs.python.org/3/library/argparse.html#type)|Automatically convert an argument to the given type|[`int`](https://docs.python.org/3/library/functions.html#int "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), `argparse.FileType('w')`, or callable function|
