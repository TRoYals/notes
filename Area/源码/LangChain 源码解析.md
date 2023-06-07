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
　
- [langchain/formatting.py](https://github.com/TRoYals/langchain/blob/18aeb720126a68201c7e3b5a617139c27c779496/langchain/formatting.py)
  
- [langchain/prompt.py](https://github.com/TRoYals/langchain/blob/18aeb720126a68201c7e3b5a617139c27c779496/langchain/prompt.py)　
  
- [langchain/llms/openai.py](https://github.com/TRoYals/langchain/blob/18aeb720126a68201c7e3b5a617139c27c779496/langchain/llms/openai.py)　
　一来就是我不会的根验证器,  [[../后端/python/library/Lib Pydantic| Pydantic]]库, 用来验证数据等. 感觉很强, 很强. 学就完事了.
　
　


　


