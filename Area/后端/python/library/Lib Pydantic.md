---
title: Lib Pydantic
date: 2023-06-07 16:55
article: false
star: false
check: 0
---

## 用pydantic做数据验证
```python
from pydantic import BaseModel, validator, root_validator, ValidationError
class MyModel(BaseModel):
name: str
age: int
@validator("age")
def age_must_be_positive(cls, value):
if value < 0:
raise ValueError("age must be positive")
return value
@root_validator
def check_name_and_age(cls, values):
name, age = values.get("name"), values.get("age")
if name == "root" and age < 18:
raise ValueError("root must be at least 18 years old")
return values
def test_check_name_and_age():
# 测试正常情况
data = {"name": "Alice", "age": 20}
result = MyModel(**data)
assert result.name == "Alice"
assert result.age == 20
# 测试 root 用户年龄太小的情况
data = {"name": "root", "age": 16}
try:
result = MyModel(**data)
except ValidationError as e:
assert "root must be at least 18 years old" in str(e)
else:
assert False, "Expected a ValidationError"
# 测试 root 用户年龄正常的情况
data = {"name": "root", "age": 20}
result = MyModel(**data)
assert result.name == "root"
assert result.age == 20
# 测试其他用户年龄太小的情况
data = {"name": "Bob", "age": -1}
try:
result = MyModel(**data)
except ValidationError as e:
assert "age must be positive" in str(e)
else:
assert False, "Expected a ValidationError"
test_check_name_and_age()
```

一个Pydantic做数据验证的模型

### validator と root_validator

`@validator` 和 `@root_validator` 是 Pydantic 中用于定义验证器的装饰器。

`@validator` 装饰器用于定义对单个字段进行验证的验证器。它的语法如下：

```python
@validator('field_name')
def validator_name(cls, v):
    ...
```

其中，`field_name` 是要验证的字段名，`validator_name` 是验证器的名称，`cls` 是模型类本身，`v` 是要验证的字段的值。验证器应该返回验证后的值，或者引发 `ValueError` 或 `TypeError` 异常。

`@root_validator` 装饰器用于定义对整个模型实例进行验证的验证器。它的语法如下：

```python
@root_validator
def validator_name(cls, values):
    ...
```

其中，`validator_name` 是验证器的名称，`cls` 是模型类本身，`values` 是一个字典，包含了模型实例中所有字段的值。验证器应该返回一个字典，表示验证后的值，或引发 `ValueError` 或 `TypeError` 异常。

## Learn by Case
### case LangChain
[[../../../源码/LangChain 源码解析|LangChain ]]中的许多地方都用到了pydantic库. 这里选择了他第一次commit时提交的数据进行分析

```python
"""Wrapper around OpenAI APIs."""
import os
from typing import Any, Dict, List, Mapping, Optional

from pydantic import BaseModel, Extra, root_validator

from langchain.llms.base import LLM


class OpenAI(BaseModel, LLM):
    """Wrapper around OpenAI large language models."""

    client: Any
    model_name: str = "text-davinci-002"
    temperature: float = 0.7
    max_tokens: int = 256
    top_p: int = 1
    frequency_penalty: int = 0
    presence_penalty: int = 0
    n: int = 1
    best_of: int = 1

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        if "OPENAI_API_KEY" not in os.environ:
            raise ValueError(
                "Did not find OpenAI API key, please add an environment variable"
                " `OPENAI_API_KEY` which contains it."
            )
        try:
            import openai

            values["client"] = openai.Completion
        except ImportError:
            raise ValueError(
                "Could not import openai python package. "
                "Please it install it with `pip install openai`."
            )
        return values

    @property
    def default_params(self) -> Mapping[str, Any]:
        """Get the default parameters for calling OpenAI API."""
        return {
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "top_p": self.top_p,
            "frequency_penalty": self.frequency_penalty,
            "presence_penalty": self.presence_penalty,
            "n": self.n,
            "best_of": self.best_of,
        }

    def __call__(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """Call out to OpenAI's create endpoint."""
        response = self.client.create(
            model=self.model_name, prompt=prompt, stop=stop, **self.default_params
        )
        return response["choices"][0]["text"]
```

1. 作者没有调用 validate_environment函数诶　
```ad-info ChatGPT
虽然代码中没有显式调用 `validate_environment` 函数，但是 Pydantic 在实例化 `OpenAI` 对象时会自动调用 `validate_environment` 函数，以保证对象的属性值是合法的。这是因为 `@root_validator` 装饰器是一个根验证器，用于对整个模型实例进行验证，而不是对单个字段进行验证。因此，无论是在实例化对象时还是在访问对象属性时，都会自动执行 `validate_environment` 函数，以确保环境变量和 Python 包的存在性。

具体来说，当我们实例化 `OpenAI` 对象时，Pydantic 会自动执行以下步骤：

1. 根据类定义创建一个空的 `OpenAI` 对象；
2. 根据类定义和传入的参数，对 `OpenAI` 对象的属性进行赋值；
3. 自动执行 `@root_validator` 装饰器定义的 `validate_environment` 方法，以验证环境变量和 Python 包的存在性；
4. 返回验证后的 `OpenAI` 对象。

因此，即使没有显式调用 `validate_environment` 方法，也可以保证它的验证逻辑能够生效。
```

2. 