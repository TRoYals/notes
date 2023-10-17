---
title: LangChain 踩坑小记
date: 2023-06-19 23:13
article: true
---

## 记录 LangChain 吃过的坑.
### prompt 相关
#### "f-string"

一般写 prompt 的时候会用\{}把变量控制住,但是有时候你不一定要用到变量, 算了, 说的有点绕, 举个例子就知道了

```python
"""I have a JSON file below : {input_language} . Now I have a new attribute " {output_language} " with its value " {test} ". You need to check if the attribute exists in the JSON keys, and to Check if the attribute exists in the JSON values(allow a little difference). After that return me a JSON file with {original attribute name or the one you find in JSON file that suits better: original attribute value or the one you find in JSON file that suits better}. Remeber to put the value in a list! And you only need to return the one you add!"""

```

注意到这里 

```python
{original attribute name or the one you find in JSON file that suits better: original attribute value or the one you find in JSON file that suits better}.
```

实际上 py 的 f-string 会在这里识别错误 (pydantic 报错),正确的做法是用\{\{}} 把不是变量的括号表示出来. 这样在用 prompt.format(\*\*kwags) 时会自动把双括号变成单括号.
