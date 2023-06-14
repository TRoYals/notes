---
title: Auto-GPT 源码解析
date: 2023-06-06 14:07
article: true
star: false
check: 0
---

# 使用方法

## 一句话概况

对于不同的选择时间点选择了对应 Commit 的 SHA 值, 比较建议的是直接拿着 SHA 去访问原代码的 git 文件. 自身的水平有限, 也不知道怎么分析源码是高效的, 但是顺着时间线一条一条的看 commit 确实就像追剧一样十分有意思. 各位不妨把这条 blog 看作一部剧情概览.

My Source Code Journey #time 2023-06-06 14:07

## 对 p 的时间的源码进行选择

本文会选取 Auto-GPT 的不同的时间点的 SHA 来进行源码分析，之所以要从之前的 commit 来分析源码，是因为你可以看到整个项目是如何从第一次[commit]()到最后落地的，整个过程十分有趣。

选择的时间点的依据就是，作者对 README 进行了较大的更新的节点。

# Commit 时间图

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

在这个 commit 中，整个 AutoGPT 的思路基本上是很清晰的了。

- browse.py
  作者在 `browse.py`中添加了能搜索网页并获取信息的功能，初步实现了通过 ChatGPT 访问网页的功能。
  在这个文件中，作者主要是通过`split_text()`和`summariz_text()`来解决 token 上限的问题.

- comands.py 　
  现在在 commands 主要实现的是访问浏览器的功能,其中比较有意思的是对长时记忆的 commit,delete,overwrite 功能. 一个值得关注的问题是什么时候使用这些功能.

- main.py 　
  当前的核心功能.

两个函数值得看一下, 一个是 `chat_with_ai` 这个函数主要实现的功能是进行 openai 的 api 调用.
着重看一下这三行.

```python
current_context = [create_chat_message("system", prompt), create_chat_message("system", f"Permanent memory: {permanent_memory}")]
current_context.extend(full_message_history[-(token_limit - len(prompt) - len(permanent_memory) - 10):])
current_context.extend([create_chat_message("user", user_input)])
```

简单来说, 就是把长时记忆和现有的 prompt 合并, 并进行访问.

另一个函数就是`execute_command`, 这个函数读取 ChatGPT 返回的信息并进行操作

### Commit 总结

这个 commit 中基本对整个 autoGPT 的底层逻辑进行了定义.
简单来说就是, 定义一个 `permant_memory`来存取 ChatGPT 返回的认为值得放入长时记忆的内容, 并讲长时记忆每次都加入到 prompt 中.

## 自动运行 - Commit 0268bb

<0268bb0b7bfe4a2ffd83d6cd909ff0cd926eac75>

[Commits · TRoYals/Auto-GPT](https://github.com/TRoYals/Auto-GPT/commits/master?before=59d31b021d80513d01e2c9a24d523dade671a8d6+1896&branch=master&qualified_name=refs%2Fheads%2Fmaster)

这次 commit 中, 值得关注一点就是从用户监督形的输入变成了程序自主运行

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

- 修 bug
- 增加了一些用户体验
- 增加了 assitant thoughts 的展示　
  简单来说, 都是一些用户体验上的东西. 但是作者的这种通过增加 continuous mode 的方式来减少风险的方式是很值得借鉴的.

## autoagent - Commit 2c6338

\<2c6338fd3b8926cc6f6984ebf4cdc89b4bea8f30>

[file - commit 2c6338](https://github.com/TRoYals/Auto-GPT/tree/2c6338fd3b8926cc6f6984ebf4cdc89b4bea8f30)

[Commits Lists - 2c6338](https://github.com/TRoYals/Auto-GPT/commits/master?after=59d31b021d80513d01e2c9a24d523dade671a8d6+1860&branch=master&qualified_name=refs%2Fheads%2Fmaster)

主要是对从上次 commit 到这一次 commit 的全部总结, 首先是加了一个 speaker 的功能, 对于本次学习没有什么帮助, 跳过.
然后是加了一个 ai_agent 的功能, 值得研究.

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

- commands.py 　
  先说说 command.py, 因为着你定义了所有对 ChatGPT 返回的 commands 的操作, 所以本质上是函数运行的直接窗口.
  增添了以下的新的 commands

1. start_agent
   字面理解就是开启一个新的 gpt
2. message_agent
3. list_agents
4. delete_agents
5. ai.evalutate_code
6. ai.improve_code
7. ai.write_tests
8. excute_python_file (什么重量级)

- agent_manager.py 　
  定义了一些与 agent 相关的操作函数

- ai_functions.py 　
  感觉还是蛮有意思的, 作者专卖写了个函数专门来处理函数的测试, 生成和提升, 这个思路可以保持. #save[Auto-GPT/ai_functions.py](https://github.com/TRoYals/Auto-GPT/blob/2c6338fd3b8926cc6f6984ebf4cdc89b4bea8f30/scripts/ai_functions.py)

- execute_code.py 　
  一个函数, 来执行 python 代码. 专门开了一个 docker 来运行代码, 这是一个好思路. 真得去学学[[docker]]了!!!
  #time 2023-06-06 17:46

- file_operation.py 　
  用来执行文件操作.
  主要是一个 safe_join(base,\*paths)函数,用来拼接路径, 感觉可以参考的.

### prompt engineering

来对现有的 commit 进行一次 prompt engineering 吧

```
CONSTRAINTS:

1. 6000-word count limit for memory
2. No user assistance

COMMANDS:

1. Google Search: "google", args: "input": "<search>"
2. Check news: "check_news", args: "source": "<news source>"
3. Memory Add: "memory_add", args: "string": "<string>"
4. Memory Delete: "memory_del", args: "key": "<key>"
5. Memory Overwrite: "memory_ovr", args: "key": "<key>", "string": "<string>"
6. Browse Website: "browse_website", args: "url": "<url>"
7. Start GPT Agent: "start_agent",  args: "name": <name>, "task": "<short_task_desc>", "prompt": "<prompt>"
8. Message GPT Agent: "message_agent", args: "key": "<key>", "message": "<message>"
9. List GPT Agents: "list_agents", args: ""
10. Delete GPT Agent: "delete_agent", args: "key": "<key>"
11. Write to file: "write_to_file", args: "file": "<file>", "text": "<text>"
12. Read file: "read_file", args: "file": "<file>"
13. Append to file: "append_to_file", args: "file": "<file>", "text": "<text>"
14. Delete file: "delete_file", args: "file": "<file>"
15. Evaluate Code: "evaluate_code", args: "code": "<code>"
16. Get Improved Code: "improve_code", args: "suggestions": "<list_of_suggestions>", "code": "<string>"
17. Write Tests: "write_tests", args: "code": "<string>", "focus": "<list_of_focus_areas>"
18. Execute Python File: "execute_python_file", args: "file": "<file>"
19. Task Complete (Shutdown): "task_complete", args: "reason": "<reason>"

RESOURCES:

1. Internet access for searches and information gathering.
2. Long Term memory management.
3. GPT-3.5 powered Agents for delegation of simple tasks.
4. File output.

PERFORMANCE EVALUATION:

1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.
2. Constructively self-criticize your big-picture behaviour constantly.
3. Reflect on past decisions and strategies to refine your approach.
4. Every command has a cost, so be smart and efficent. Aim to complete tasks in the least number of steps.

RESPONSE FORMAT:
{
"command":
{
"name": "command name",
"args":
{
"arg name": "value"
}
},
"thoughts":
{
"text": "thought",
"reasoning": "reasoning",
"plan": "short bulleted long-term plan",
"criticism": "constructive self-criticism"
"speak": "thoughts summary to say to user"
}
}

```

感觉还是一目了然的.

## 中场休息 - 部分其他 commit

现在所在的 commit [list+1861](https://github.com/TRoYals/Auto-GPT/commits/master?before=59d31b021d80513d01e2c9a24d523dade671a8d6+1861&branch=master&qualified_name=refs%2Fheads%2Fmaster)

- commit [ef656a0](https://github.com/TRoYals/Auto-GPT/commit/ef656a0f778ef7803f26164aa6484aba5c001ece) 使用.env 替代 keys, 确实感觉要安全不少啊, 自己之前使用 config.ini 来控制敏感信息, 不好的地方就是每次都要指定到变量, 很麻烦.

- commit [d19b7be](https://github.com/TRoYals/Auto-GPT/commit/d19b7bedd14fb3a6ce743342e2b4ff3877ac2401) [[../后端/Docker/Docker|Docker]]file 人永不缺席 233

- commit [9ff7e59](https://github.com/TRoYals/Auto-GPT/commit/9ff7e5954b19db2f69708c2f6c949f033c851bf2) 这个佬(**Taytay**)感觉很厉害, 他在这个 commit 中更新了一个 config 类来管理 选择的模型状态, 同时, 他在 TODO: 中说明了未来可以用 LangChain 训练的模型, 这个佬对 LangChain 也有研究! 后续将会一直关注他.

- commit [tree/7fd2ce2](https://github.com/TRoYals/Auto-GPT/tree/7fd2ce2bc647f7502f6b39ea08cf8dda892ea1d9)

对 Taytay 的更新做一次简单的总结, Taytay 意识到了对模型的选择上不能只局限在 ChatGPT-4 上, 他设定了一个[config.py](https://github.com/TRoYals/Auto-GPT/blob/7fd2ce2bc647f7502f6b39ea08cf8dda892ea1d9/scripts/config.py) 来装各种模型的信息以及需要导入的 env. 并且他在这个模型中使用了 一个 class Singleton(type) 来确保只有一个 instance.

还定义了一个[AIConfig.py](https://github.com/TRoYals/Auto-GPT/blob/7fd2ce2bc647f7502f6b39ea08cf8dda892ea1d9/scripts/ai_config.py), 来记录 ai 保存的结果, 类似于一个中间件吧. 在[main.py](https://github.com/TRoYals/Auto-GPT/blob/7fd2ce2bc647f7502f6b39ea08cf8dda892ea1d9/scripts/main.py) 中定义了 fn: construct_prompt 来快速生成 ai 对话 prompt.

## From Merge pull Taytay Commit ea91201 　

- commit [ea91201](https://github.com/TRoYals/Auto-GPT/commit/ea9120180e704d7b8b7b4385116b676ce4b2ae77)

merge 了 Taytay 的 commits. 主要是新加了一些[[测试用例]], 感觉自己对测试用例方面的知识一直都不是很够, 这些内容还是很有参考价值的.

感觉可以基于这个版本做一些简单的测试了, 到目前为止的代码还是很快迁移部署的.

- commit [f20d6f3](https://github.com/TRoYals/Auto-GPT/commit/f20d6f3fdb731c43910ba49916a7c8e2e1fd9eb5) Prompt Engineering

  这个老哥, 做了一些 prompt 改进, 主要是处理了 JSON 文件中单双引号的问题, 还有就是把 None 和 NaN 的 Value 变成 null 的问题. 这是一个好思路. AI 可能会认为这些是 str, 实际上并不是

- commit [f2ba7f2+](https://github.com/TRoYals/Auto-GPT/commit/f2ba7f21c510fabe226fac661df0e9112674708a) 　
  　这个老哥把谷歌 search method 变成了 Google Custom Search API, 如果以后需要实现 online search 功能的话感觉可以参考.

现在所在的 [commit-lists](https://github.com/TRoYals/Auto-GPT/commits/master?before=59d31b021d80513d01e2c9a24d523dade671a8d6+1756&branch=master&qualified_name=refs%2Fheads%2Fmaster)

- commit [1b7b367+-](https://github.com/TRoYals/Auto-GPT/commit/1b7b367ce9e0455caf7ec2efbb0b5f4701bd2a51)

  这个老哥我受不了了!!! AndresCdo 老哥, 一直在那里修改 coding style, 就是加空行之类的... 这也行(我也能上@\_@)　(我怀疑这个老哥是个完美主义者...收回前面的评价)

进入垃圾时间了....不过话虽这么说, 才到 04/04/23, 才过了几天啊, 有点恐怖.

看到这里了 [commit-list+1721](https://github.com/TRoYals/Auto-GPT/commits/master?before=59d31b021d80513d01e2c9a24d523dade671a8d6+1721) 还有 1k 多条, 但感觉后面会快很多.

- commit [a4f130f](https://github.com/TRoYals/Auto-GPT/commit/a4f130ff602b89e1dac571362b34db5b8cb41429) 　
  　看着像是俄国老哥(Slavakurilyak), 更新了`browse.py`的[[代码安全性|安全性]]和鲁棒性! 重点关注!
  　简单来说, 增加了一些 url 的验证, 之后自己也要做爬虫项目, 大概率是要用上的. #time 2023-06-07 14:27

- commit [1e47328](https://github.com/TRoYals/Auto-GPT/commit/1e4732807931f815feb3f6dfab22b5f7c4d0ce15) 　　
  　俄国老哥继续发力, 增加了一个 Search_file 的功能, 能查找本地文件了! 一个小 tips

```python
def search_files(dir):
founr_files = []
serarch_dir = safe_join(working_dir, dir)
for root,_,files in os.walk(search_dir):
    for file in files:
		if file.startwith("."):
			continue
		relative_path =  os.path.relpath(os.path.join(root,file),working_dir)
		founr_files.append(relative_path)

return found_files
```

其实 遍历文件 的操作操作过很多次了, 但看别人的代码还是能学到不少东西,

1.  处理 .file 文件, 确实这个应该考虑
2.  os.walk() 操作, 自己都是用 os.listdir() 来操作的,os.walk 可以操作整个文件夹, 包括子列表. 要注意的是其返回的是一个三元组! 对于返回元组类型的文档都要特别关注一下.
3.  os.path.relpath() 的使用, 看看别人是怎么用的. 但好像没什么特别要注意的地方.

不想看了!!! 休息片刻, 去看看[[LangChain 源码解析-按提交顺序]] #time 2023-06-07 14:45

回来了！ #time
2023-06-12 16:42 继续看

- commit [475671d](https://github.com/TRoYals/Auto-GPT/commit/475671d1e846a370a38e2044a73aaa1da417fd9a)
  [[Pincone]]加入！在处理长时间记忆时，可以用 Pinecone 来做处理。
  问题： 什么是 Pincone？可以参考这篇文章[Pinecone 和 LangChain：大语言模型应用程序开发利器 - 知乎](https://zhuanlan.zhihu.com/p/626349478)
  [Pinecone：大模型引发爆发增长的向量数据库，AI Agent 的海马体-36 氪](https://36kr.com/p/2233027665457281)
