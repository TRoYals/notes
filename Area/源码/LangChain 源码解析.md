---
title: LangChain 源码解析
date: 2023-06-07 14:45
article: true
star: false
check: 0
---

开始时间 2023-06-07 14:45

需求导向读源码, good Luck

# 源码概览
[fork](https://github.com/TRoYals/langchain)时间 #time 2023-06-07 14:47

commit数 2384条 ,[ initail commit](https://github.com/TRoYals/langchain/commits/master?after=b3ae6bcd3f42ec85ee65eb29c922ab22a17a0210+2380&branch=master&qualified_name=refs%2Fheads%2Fmaster)时间 2022-10-25 

一般贴了SHA的地方就表示在vscode中运行了当前版本

# 开搞
## initial commit 18aeb72
### 基本描述

其实第一次commit的时候就是一个很完整的项目了...

从文件开始慢慢看吧. 这个initial commit可能要看很久



- commit [tree/18aeb72](https://github.com/TRoYals/langchain/tree/18aeb720126a68201c7e3b5a617139c27c779496)　
这个人的代码明显就比[[Auto-GPT源码解析|auto-gpt]]的要成熟的多...我直接狂学!

贴个SHA\<18aeb720126a68201c7e3b5a617139c27c779496>

代码结构: 
```
.
├── docs
│   ├── Makefile
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   ├── modules
│   │   ├── chains.rst
│   │   ├── llms.rst
│   │   └── prompt.rst
│   └── requirements.txt
├── examples
│   ├── llm_math.ipynb
│   ├── self_ask_with_search.ipynb
│   └── simple_prompts.ipynb
├── langchain
│   ├── VERSION
│   ├── __init__.py
│   ├── chains
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── llm.py
│   │   ├── llm_math
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── prompt.py
│   │   ├── python.py
│   │   ├── self_ask_with_search
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── prompt.py
│   │   └── serpapi.py
│   ├── formatting.py
│   ├── llms
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── cohere.py
│   │   └── openai.py
│   └── prompt.py
├── pyproject.toml
├── readthedocs.yml
├── requirements.txt
├── setup.py
├── test_requirements.txt
└── tests
    ├── __init__.py
    ├── integration_tests
    │   ├── __init__.py
    │   ├── chains
    │   │   ├── __init__.py
    │   │   ├── test_self_ask_with_search.py
    │   │   └── test_serpapi.py
    │   └── llms
    │       ├── __init__.py
    │       ├── test_cohere.py
    │       └── test_openai.py
    └── unit_tests
        ├── __init__.py
        ├── chains
        │   ├── __init__.py
        │   ├── test_base.py
        │   ├── test_llm.py
        │   ├── test_llm_math.py
        │   └── test_python.py
        ├── data
        │   └── prompts
        │       ├── prompt_extra_args.json
        │       ├── prompt_missing_args.json
        │       └── simple_prompt.json
        ├── llms
        │   ├── __init__.py
        │   ├── fake_llm.py
        │   └── test_cohere.py
        ├── test_formatting.py
        └── test_prompt.py

```

### 从 /langchain/ 开始　　
```
├── langchain
│   ├── VERSION
│   ├── __init__.py
│   ├── chains
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── llm.py
│   │   ├── llm_math
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── prompt.py
│   │   ├── python.py
│   │   ├── self_ask_with_search
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── prompt.py
│   │   └── serpapi.py
│   ├── formatting.py
│   ├── llms
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── cohere.py
│   │   └── openai.py
│   └── prompt.py
```

- [langchain/__init__.py](https://github.com/TRoYals/langchain/blob/18aeb720126a68201c7e3b5a617139c27c779496/langchain/__init__.py)　　　
  作者把__init__.py当作了一个 entrypoint, 感觉是个好思路, 有学到　

  
- [langchain/llms/openai.py+base.py](https://github.com/TRoYals/langchain/blob/18aeb720126a68201c7e3b5a617139c27c779496/langchain/llms/openai.py)　
　一来就是我不会的根验证器,  [[../后端/python/library/Lib Pydantic| Pydantic]]库, 用来验证数据等. 感觉很强, 很强. 学就完事了.同时还用到了[[../后端/python/library/Lib ABC| ABC]]抽象基类, 并将二者结合来保证数据类型的一致性!看的出来, 作者很喜欢类型体操, 一眼大佬!

- langchain/chains　　
 这个Chains文件夹里装的都是啥??? 感觉很有意思(大概), llms里基本就是一些语言模型的交互, 这里的才是重点!　
- langchain/chains/base.py
	这里是所有 chains的abc. 

- langchain/chains/python.py
  作者定义了一条**Chain** 去run pycode! 和autogpt的思路几乎一样, 但是autogpt是用Docker实现的.

## Version 0032 -commit 180
时间来到08/12/22. 选择这个版本来分析源码
\<e2e501aa06163a1cbd22efa8890b0b586db6e059>

这个版本决定完全钻研透. 从单元测试到整体测试什么的都得学!

其实学到这里 #time 
2023-06-09 17:06, 基本上就可以写一份python项目指南了.

python项目搭建