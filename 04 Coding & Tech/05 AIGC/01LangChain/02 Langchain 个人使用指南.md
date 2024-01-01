---
title: Langchain 个人使用指南
article: true
date: 2023-06-18 15:54
---

```tasks

(path includes 开源项目)
explain
```

主要是根据官方文档来的

## modules

### llms

### Prompts

#### output_parsers

output_parsers 是一个 ABC, 主要的方法有这些:  
`<class:output_parsers>.get_format_instructions()`  
会返回所实用的 Output parser 的 Instructions.

`<class:output_parsers>.dict()` 会返回一个类似如下的语句

```
{'format': '%Y-%m-%dT%H:%M:%S.%fZ', '_type': 'datetime'}
```

`<class:output_parsers>.parse(response　:str)` 对返回的文字按照所选择的 parse 进行信息提取.

##### CommaSeparatedListOutputParser()

```python
output_parser = CommaSeparatedListOutputParser()
format_instructions =output_parser.get_format_instructions()

prompt = PromptTemplate(
template="List five {subject}.\n{format_instructions}",
input_variables=["subject"],
partial_variables={"format_instructions":format_instructions}
)
```

就是在 prompt 后加了一句如下的话:

```text
Your response should be a list of comma separated values, eg: `foo, bar, baz`
```

然后对于返回的语句使用 `output_parser.parse(output)`,就可以抓到一个列表.

如果使用的是 ChatModel 的话,需要进行如下操作

```python
chatTemp:str =  prompt.format(subject="ice cream flavors")
AIMessage = AIMessagePromptTemplate.from_template(chatTemp).format_messages()
model = ChatOpenAI(temperature=0)
output = model(AIMessage)
output_parser.parse(output.content) #即可以获得列表
```

##### DatetimeOutputParser()

使用方法同上,具体来说就是在原有的 prompt 上加了一句如下的话:

```
Write a datetime string that matches the following pattern: "%Y-%m-%dT%H:%M:%S.%fZ". Examples: 1290-12-08T11:55:33.743538Z, 1764-07-13T00:01:08.462257Z, 1095-01-18T11:35:53.457565Z
```

使用同样的 parse 获取时间

```python
output_parser = DatetimeOutputParser()
output_parser.parse(output)
#output: datetime.datetime(2009, 1, 3, 18, 15, 5)
```

使用 `<class:datetime.datetime>.strftime("%Y-%m-%d %H:%M:%S")` 将时间变成自己想要的时间

```python
formatted_date = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Answer: {formatted_date}")
#output: Answer: 2009-01-03 18:15:05
```

##### EnumOutputParser()

可以设置一个属性

```python
from langchain.output_parsers.enum import EnumOutputParser
from enum import Enum

class Colors(Enum):
RED = "red"
GREEN = "green"
BLUE = "blue"

parser = EnumOutputParser(enum=Colors)
parser.parse("red") #<Colors.RED: 'red'>
parser.parse(" green") #<Colors.GREEN: 'green'>
parser.parse(" blue\n") #<Colors.BLUE: 'blue'>
parser.parse("yellow") #报错
```

感觉没什么用啊...

##### PydanticOutputParser()

这是 PydanticOutputParser 的一些内置函数

```python
    def get_format_instructions(self) -> str:
        schema = self.pydantic_object.schema()

        # Remove extraneous fields.
        reduced_schema = schema
        if "title" in reduced_schema:
            del reduced_schema["title"]
        if "type" in reduced_schema:
            del reduced_schema["type"]
        # Ensure json in context is well-formed with double quotes.
        schema_str = json.dumps(reduced_schema)

        return PYDANTIC_FORMAT_INSTRUCTIONS.format(schema=schema_str)
```

```python
  def parse(self, text: str) -> T:
        try:
            # Greedy search for 1st json candidate.
            match = re.search(
                r"\{.*\}", text.strip(), re.MULTILINE | re.IGNORECASE | re.DOTALL
            )
            json_str = ""
            if match:
                json_str = match.group()
            json_object = json.loads(json_str, strict=False)
            return self.pydantic_object.parse_obj(json_object)

        except (json.JSONDecodeError, ValidationError) as e:
            name = self.pydantic_object.__name__
            msg = f"Failed to parse {name} from completion {text}. Got: {e}"
            raise OutputParserException(msg)
```

感觉这个应该是最有用的了!

一个 eg

```python
# Here's another example, but with a compound typed field.
class Actor(BaseModel):
    name: str = Field(description="name of an actor")
    film_names: List[str] = Field(description="list of names of films they starred in")

actor_query = "Generate the filmography for a random actor."

parser = PydanticOutputParser(pydantic_object=Actor)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

_input = prompt.format_prompt(query=actor_query)

output = model(_input.to_string())

parser.parse(output)
```

```text
Actor(name='Tom Hanks', film_names=['Forrest Gump', 'Saving Private Ryan', 'The Green Mile', 'Cast Away', 'Toy Story'])
```

##### OutputFixingParser()

挺抽象的,包装一个 parser 并修改它的错误.  
觉得挺好玩的,直接放源码了

```python
class OutputFixingParser(BaseOutputParser[T]):
    """Wraps a parser and tries to fix parsing errors."""

    parser: BaseOutputParser[T]
    retry_chain: LLMChain

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        parser: BaseOutputParser[T],
        prompt: BasePromptTemplate = NAIVE_FIX_PROMPT,
    ) -> OutputFixingParser[T]:
        chain = LLMChain(llm=llm, prompt=prompt)
        return cls(parser=parser, retry_chain=chain)

    def parse(self, completion: str) -> T:
        try:
            parsed_completion = self.parser.parse(completion)
        except OutputParserException as e:
            new_completion = self.retry_chain.run(
                instructions=self.parser.get_format_instructions(),
                completion=completion,
                error=repr(e),
            )
            parsed_completion = self.parser.parse(new_completion)

        return parsed_completion

    def get_format_instructions(self) -> str:
        return self.parser.get_format_instructions()
```

就是再 call 一次 ai,让 ai 帮我们 fix

```
NAIVE_FIX = """Instructions:
--------------
{instructions}
--------------
Completion:
--------------
{completion}
--------------

Above, the Completion did not satisfy the constraints given in the Instructions.
Error:
--------------
{error}
--------------

Please try again. Please only respond with an answer that satisfies the constraints laid out in the Instructions:"""

```

感觉还蛮有意思的,就是 ai 每次都会返回正确的吗? 保持怀疑.

#save 这个 OutputFixingParser 的调用方法还蛮有意思的感觉以后可以看源码来学习.

##### RetryOutputParser()

不想总结了 有时间在做吧

- [x] 总结这一章 🛫 2023-06-19 📅 2023-06-25 ✅ 2023-11-14

##### StructuredOutputParser()

弃用

### Memory

#### ChatMessageHistory()

串起来了

```python
from langchain.memory import ChatMessageHistory
history = ChatMessageHistory()
history.add_user_message("hi!")
history.add_ai_message("whats up?")

print(history.messages)
# [HumanMessage(content='hi!', additional_kwargs={}, example=False), AIMessage(content='whats up?', additional_kwargs={}, example=False)]
```

#### ConversationBufferMemory()

另一种 Memory. 感觉不如 ChatMessageHistory.

```python
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("hi!")
memory.chat_memory.add_ai_message("whats up?")
memory.load_memory_variables({})
# {'history': 'Human: hi!\nAI: whats up?'}
memory = ConversationBufferMemory(return_messages=True)
memory.chat_memory.add_user_message("hi!")
memory.chat_memory.add_ai_message("whats up?")
memory.load_memory_variables({})
# {'history': [HumanMessage(content='hi!', additional_kwargs={}, example=False), AIMessage(content='whats up?', additional_kwargs={}, example=False)]}
```

只有 history 一个属性?,我不信. 好吧, 还真是....

可以通过 memory.chat_memory.add_message(\*history.messages)  
把 chatmessge 加入到 buffer 里

#### 在 [[#Chains]] 中使用 Memory

[[#ConversationChain()]]

##### adding_memory

... 难崩

```python
template = """You are a chatbot having a conversation with a human.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")
```

通过 memory 类型名:  
类型名: <class 'langchain.memory.buffer.ConversationBufferMemory'>  
可选参数:\['lc_kwargs', 'chat_memory', 'output_key', 'input_key', 'return_messages', 'human_prefix', 'ai_prefix', 'memory_key']  
必须参数:\[]

```python
llm_chain = LLMChain(
    llm=OpenAI(),
    prompt=prompt,
    verbose=True,
    memory=memory,
)
llm_chain.predict(human_input="Hi there my friend")
# " Hi there! It's great to meet you! How are you doing today?"
llm_chain.predict(human_input="Not too bad - how are you?")
# " I'm doing great, thank you for asking!"
```

##### adding_memory_with_doc_and_memory

```ad-info
可能从不止一个地方导入 memory
```

```python
template = """You are a chatbot having a conversation with a human.

Given the following extracted parts of a long document and a question, create a final answer.

{context}

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input", "context"],
    template=template
)
memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")
chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff", memory=memory, prompt=prompt)

```

然后就可以不停的问了

```python
query = "What did the president say about Justice Breyer"
chain({"input_documents": docs, "human_input": query}, return_only_outputs=True)
print(chain.memory.buffer)
```

注意这个时候,可以不断的重复 query 和 chain 的步骤,这个时候会同时更新 doc 和 memory.

但是这样也同时存在 3 个问题

- [x] memory 超出怎么办 (过长)? ✅ 2023-11-14
- [ ] doc 过长怎么办?
- [ ] 超出 4096 怎么办?

##### agent_with_memory

##### agent_with_memory_in_db

#### 保存 memory history

```python
from langchain.schema import messages_from_dict, messages_to_dict
dicts = messages_to_dict(history.messages)

new_messages = messages_from_dict(dicts)
```

### Chains

#### Add Memory to Chains

就是看怎么把 message 保存

```python

```

##### ConversationChain()

##### load_qa_chain()
