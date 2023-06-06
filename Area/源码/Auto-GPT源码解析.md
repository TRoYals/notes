---
title: Auto-GPT
date: 2023-06-06 14:07
article: false
star: false
check: 0
---

# 使用方法
## 一句话概况
对于不同的选择时间点选择了对应Commit的SHA值, 比较建议的是直接拿着SHA去访问原代码的git文件. 自身的水平有限, 也不知道怎么分析源码是高效的, 但是顺着时间线一条一条的看commit确实就像追剧一样十分有意思. 各位不妨把这条blog看作一部剧情概览. 


## 对不同的时间的源码进行选择
本文会选取Auto-GPT的不同的时间点的SHA来进行源码分析，之所以要从之前的commit来分析源码，是因为你可以看到整个项目是如何从第一次[commit]()到最后落地的，整个过程十分有趣。

选择的时间点的依据就是，作者对README进行了较大的更新的节点。


# Commit时间图
## Tidy up Codebase - Commit fc6c7bd
\<fc6c7bd8c4e9bf8d6183fc9d1fe0a1140756f3eb>

[Tides up codebase. · TRoYals/Auto-GPT@fc6c7bd](https://github.com/TRoYals/Auto-GPT/commit/fc6c7bd8c4e9bf8d6183fc9d1fe0a1140756f3eb)

[TRoYals/Auto-GPT at fc6c7bd8c4e9bf8d6183fc9d1fe0a1140756f3eb](https://github.com/TRoYals/Auto-GPT/tree/fc6c7bd8c4e9bf8d6183fc9d1fe0a1140756f3eb)


```
├── browse.py
├── commands.py
├── keys.py
├── main.py
└── memory.py
```
在这个commit中，整个AutoGPT的思路基本上是很清晰的了。

- browse.py
作者在 `browse.py`中添加了能搜索网页并获取信息的功能，初步实现了通过ChatGPT访问网页的功能。
在这个文件中，作者主要是通过`split_text()`和`summariz_text()`来解决token上限的问题.

- comands.py　
现在在commands主要实现的是访问浏览器的功能,其中比较有意思的是对长时记忆的commit,delete,overwrite功能. 一个值得关注的问题是什么时候使用这些功能.

- main.py　
当前的核心功能.

两个函数值得看一下, 一个是 `chat_with_ai` 这个函数主要实现的功能是进行openai的api调用.
着重看一下这三行.

```python
current_context = [create_chat_message("system", prompt), create_chat_message("system", f"Permanent memory: {permanent_memory}")]
current_context.extend(full_message_history[-(token_limit - len(prompt) - len(permanent_memory) - 10):]) current_context.extend([create_chat_message("user", user_input)])
```

简单来说, 就是把长时记忆和现有的prompt合并, 并进行访问.

另一个函数就是`execute_command`, 这个函数读取ChatGPT返回的信息并进行操作

### Commit 总结
这个commit中基本对整个autoGPT的底层逻辑进行了定义.
简单来说就是, 定义一个 `permant_memory`来存取 ChatGPT返回的认为值得放入长时记忆的内容, 并讲长时记忆每次都加入到prompt中.

## 自动运行 Commit 0268bb 
<0268bb0b7bfe4a2ffd83d6cd909ff0cd926eac75>

[Commits · TRoYals/Auto-GPT](https://github.com/TRoYals/Auto-GPT/commits/master?before=59d31b021d80513d01e2c9a24d523dade671a8d6+1896&branch=master&qualified_name=refs%2Fheads%2Fmaster)


这次commit中, 值得关注一点就是从用户监督形的输入变成了程序自主运行

```ad-info
Implements continuous mode!

Experimental and potentially dangerous, use at own risk.
Runs auto-gpt without user authorisation for each turn.
```


```
├── browse.py
├── chat.py
├── commands.py
├── data
│   └── prompt.txt
├── data.py
├── keys.py
├── main.py
├── memory.py
└── spinner.py
```

顺带说一下相较上一个节点做了哪些改进.
- 修bug
- 增加了一些用户体验
- 增加了 assitant thoughts的展示　
简单来说, 都是一些用户体验上的东西. 但是作者的这种通过增加continuous mode的方式来减少风险的方式是很值得借鉴的.

## autoagent Commit 2c6338
\<2c6338fd3b8926cc6f6984ebf4cdc89b4bea8f30>

[file - commit 2c6338](https://github.com/TRoYals/Auto-GPT/tree/2c6338fd3b8926cc6f6984ebf4cdc89b4bea8f30)

[Commits Lists - 2c6338](https://github.com/TRoYals/Auto-GPT/commits/master?after=59d31b021d80513d01e2c9a24d523dade671a8d6+1860&branch=master&qualified_name=refs%2Fheads%2Fmaster)

主要是对从上次commit到这一次commit的全部总结

```
scripts
    ├── agent_manager.py
    ├── ai_functions.py
    ├── browse.py
    ├── chat.py
    ├── commands.py
    ├── config.py
    ├── data
    │   └── prompt.txt
    ├── data.py
    ├── execute_code.py
    ├── file_operations.py
    ├── keys.py
    ├── main.py
    ├── memory.py
    ├── speak.py
    └── spinner.py
```

