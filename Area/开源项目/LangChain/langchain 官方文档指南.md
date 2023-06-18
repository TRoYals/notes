---
title: langchain 官方文档指南
date: 2023-06-14 12:55
article: true
---

## Memory

[Memory — 🦜🔗 LangChain 0.0.200](https://python.langchain.com/en/latest/modules/memory/getting_started.html)
使用 `buffer` 作为 Memory ！

### ChatMessageHistory

```python
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()

history.add_user_message("hi!")

history.add_ai_message("whats up?")
```

history.messages

[HumanMessage(content='hi!', additional_kwargs={}, example=False),
AIMessage(content='whats up?', additional_kwargs={}, example=False)]

### ConversationBufferMemory

将对话记录保存为 Buffer 流

### Use memories in Chain

## Indexes

## Chain

[Chains — 🦜🔗 LangChain 0.0.200](https://python.langchain.com/en/latest/modules/chains/getting_started.html)

```ad-info
Extending the previous example, we can construct an LLMChain which takes user input, formats it with a PromptTemplate, and then passes the formatted response to an LLM.
```

### different ways of calling chains

[different ways of calling Chains](https://python.langchain.com/en/latest/modules/chains/getting_started.html#different-ways-of-calling-chains)

### Add memeory to Chains

```ad-info
Chain supports taking a BaseMemory object as its memory argument, allowing Chain object to persist data across multiple calls. In other words, it makes Chain a stateful object.

```

```python
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

conversation = ConversationChain(
    llm=chat,
    memory=ConversationBufferMemory()
)

conversation.run("Answer briefly. What are the first 3 colors of a rainbow?")
# -> The first three colors of a rainbow are red, orange, and yellow.
conversation.run("And the next 4?")
# -> The next four colors of a rainbow are green, blue, indigo, and violet.
```

简单来说， memory 就是一个存储对象，可以存储一些数据，然后在后续的调用中，可以使用这些数据。 在后续 Memory 的章节中，会详细介绍。

### Debug Chain

设置 Debug 参数可以显示 Chain 的内部信息。
在使用 Chain 的时候，可以设置 debug 参数，来显示 Chain 的内部信息，具体来说就是设置`verbose=True`。

### Combine Chains

看代码就应该很清楚了

先创造一个 Chain

```python
second_prompt = PromptTemplate(
    input_variables=["company_name"],
    template="Write a catchphrase for the following company: {company_name}",
)
chain_two = LLMChain(llm=llm, prompt=second_prompt)
```

然后把这个 Chain 作为一个参数传递给另一个 Chain

```python
from langchain.chains import SimpleSequentialChain
overall_chain = SimpleSequentialChain(chains=[chain, chain_two], verbose=True)

# Run the chain specifying only the input variable for the first chain.
catchphrase = overall_chain.run("colorful socks")
print(catchphrase)
```

### create a custom Chain with **Chain** class

Steps to create a custom chain:

1. Start by subclassing the Chain class.
2. Fill out the `input_keys` and `output_keys` class attributes.
3. Add the `_call` method that shows how to execute the chain.

An example:

```python
from langchain.chains import LLMChain
from langchain.chains.base import Chain

from typing import Dict, List

class ConcatenateChain(Chain):
    chain_1: LLMChain
    chain_2: LLMChain

    @property
    def input_keys(self) -> List[str]:
        # Union of the input keys of the two chains.
        all_input_vars = set(self.chain_1.input_keys).union(set(self.chain_2.input_keys))
        return list(all_input_vars)

    @property
    def output_keys(self) -> List[str]:
        return ['concat_output']

    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        output_1 = self.chain_1.run(inputs)
        output_2 = self.chain_2.run(inputs)
        return {'concat_output': output_1 + output_2}
```

运行

```python
prompt_1 = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
chain_1 = LLMChain(llm=llm, prompt=prompt_1)

prompt_2 = PromptTemplate(
    input_variables=["product"],
    template="What is a good slogan for a company that makes {product}?",
)
chain_2 = LLMChain(llm=llm, prompt=prompt_2)

concat_chain = ConcatenateChain(chain_1=chain_1, chain_2=chain_2)
concat_output = concat_chain.run("colorful socks")
print(f"Concatenated output:\n{concat_output}")
```

```
Concatenated output:


Funky Footwear Company

"Brighten Up Your Day with Our Colorful Socks!"
```

### HOW-TO GUIDEs
