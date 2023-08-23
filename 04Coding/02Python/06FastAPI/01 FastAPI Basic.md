---
title: 01 Why FastAPI
date: 2023-06-26 21:59
article: false
tags:
---

## Resources

[First Steps - FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) 官方文档  
[why FastAPI](https://hyp.is/rrHD_hQpEe6rkq8Wtd7YHg/fastapi.tiangolo.com/async/)  
[Getting Started Step-By-Step | JSON Schema](https://json-schema.org/learn/getting-started-step-by-step)  

## FastAPI 官方文档整理

[First Steps - FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)  

### First Step

run server: `uvicorn main:app --reload` 

### Path & Query Parameters & Request Body Concept

#### 什么是 Path parameters
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}
```

ps: 注意顺序 (同 Django)

#### Path parameters containing paths

FastAPI 支持把一部分路径作为参数输出.(support path parameter)

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

```ad-tip
You could need the parameter to contain `/home/johndoe/myfile.txt`, with a leading slash (`/`).

In that case, the URL would be: `/files//home/johndoe/myfile.txt`, with a double slash (`//`) between `files` and `home`.
```

#### Query Parameters

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

#### Request Body

What FastAPI do?

```ad-info
## Results[¶](https://fastapi.tiangolo.com/tutorial/body/#results "Permanent link")

With just that Python type declaration, **FastAPI** will:

- Read the body of the request as JSON.
- Convert the corresponding types (if needed).
- Validate the data.
    - If the data is invalid, it will return a nice and clear error, indicating exactly where and what was the incorrect data.
- Give you the received data in the parameter `item`.
    - As you declared it in the function to be of type `Item`, you will also have all the editor support (completion, etc) for all of the attributes and their types.
- Generate [JSON Schema](https://json-schema.org/) definitions for your model, you can also use them anywhere else you like if it makes sense for your project.
- Those schemas will be part of the generated OpenAPI schema, and used by the automatic documentation UIs.
```

对于生成的 JsonSchemas 可以在 /docs 里查看.

### Query Parameters and String Validations

[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameters-and-string-validations "Permanent link")

#### 什么是 Query Parameters Validation
	对 Query Parameters添加 Validation:

  Additional validation[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#additional-validation "Permanent link")

比如, 我们想要对 query parameters 添加一个条件: 长度不能超过 50:  

```python
from typing import Annotated
from fastapi import FastAPI, Query
app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

```

注意这里:`async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):` 这里实际是把 `query` 封装进了 `Annotated[<type>,"Some description"]` 里, and it works.

也可以使用老版 (old version) 的调用方式:`async def read_items(q: str | None = Query(default=None, max_length=50)):`

但是作者建议还是用新版的, 意思就是推荐用 `Annotated` type, 原因如下:

```ad-info
### Advantages of `Annotated`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#advantages-of-annotated "Permanent link")

**Using `Annotated` is recommended** instead of the default value in function parameters, it is **better** for multiple reasons. 🤓

The **default** value of the **function parameter** is the **actual default** value, that's more intuitive with Python in general. 😌

You could **call** that same function in **other places** without FastAPI, and it would **work as expected**. If there's a **required** parameter (without a default value), your **editor** will let you know with an error, **Python** will also complain if you run it without passing the required parameter.

When you don't use `Annotated` and instead use the **(old) default value style**, if you call that function without FastAPI in **other place**, you have to **remember** to pass the arguments to the function for it to work correctly, otherwise the values will be different from what you expect (e.g. `QueryInfo` or something similar instead of `str`). And your editor won't complain, and Python won't complain running that function, only when the operations inside error out.

Because `Annotated` can have more than one metadata annotation, you could now even use the same function with other tools, like [Typer](https://typer.tiangolo.com/). 🚀
```

#### Query Parameters Validation 支持的参数

min_length max_length regex

#### make it Required  

1. `async def read_items(q: Annotated[str|None, Query(min_length=3)]):`  
2. `async def read_items(q: Annotated[str | None, Query(min_length=3)] =...):`
3. `from pydantic import Required`  
	`async def read_items(q: Annotated[str, Query(min_length=3)] = Required):`
 
#### Declare more metadata

Just look at the <font color="#ff0000">source Code </font>of the `Query` and you will get the answer.

##### Alias parameters
```python
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

```

这样就可以 get 到 "item-query" 并赋予给 q 了

```ad-warning
因为在py中不能以 item-query 为变量名
async def read_items(~~item-query~~ : Annotated[str | None, Query()] = None):
```

### Path Parameters and Numeric Validations

[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#path-parameters-and-numeric-validations "Permanent link")

基本上和上一节的内容一样, 只不过这一节把验证的对象从 `Query` 换成了 `Path`

#### Number validations: greater than or equa

[¶](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-or-equal "Permanent link")

### Body
#### Singular values in body
```python
@app.put("/items/{item_id}") 
async def update_item( item_id: int, item: Item, user: User, importance: Annotated[int, Body(gt=0)] ): 
	results = {"item_id": item_id, "item": item, "user": user, "importance": importance} 
	return results
```

如果不用 `Annoted[int,Body()]` 那么 FastAPI 会把他读成 Query.

```ad-info
`Body` also has all the same extra validation and metadata parameters as `Query`,`Path` and others you will see later.
```
#### Embed a single body parameter

[¶](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter "Permanent link")

这里看不太懂, 哦, 还好吧.

#### Fields

用 `pydantic` 中的 `Field` 来验证每个 body.

```ad-info
Actually, `Query`, `Path` and others you'll see next create objects of subclasses of a common `Param` class, which is itself a subclass of Pydantic's `FieldInfo` class.

And Pydantic's `Field` returns an instance of `FieldInfo` as well.

`Body` also returns objects of a subclass of `FieldInfo` directly. And there are others you will see later that are subclasses of the `Body` class.

Remember that when you import `Query`, `Path`, and others from `fastapi`, those are actually functions that return special classes.
```

#### Nested Models

Body - Nested Models[¶](https://fastapi.tiangolo.com/tutorial/body-nested-models/#body-nested-models "Permanent link")  
核心内容了, 一定要看啊!!

### Declare Request Example Data

[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#declare-request-example-data "Permanent link")

#### use Config to set the default

Use [[../04python三方库/01 pydantic|01 pydantic]] to  
You can declare examples of the data your app can receive.

Here are several ways to do it.

Pydantic `schema_extra`[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#pydantic-schema_extra "Permanent link")

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

```

You can declare an `example` for a Pydantic model using `Config` and `schema_extra`, as described in [Pydantic's docs: Schema customization](https://pydantic-docs.helpmanual.io/usage/schema/#schema-customization):

That extra info will be added as-is to the output **JSON Schema** for that model, and it will be used in the API docs.

```ad-tip
You could use the same technique to extend the JSON Schema and add your own custom extra info.

For example you could use it to add metadata for a frontend user interface, etc.
```

#### use the `example ` variable to set the default value.

```python
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results

```

#### Technical Details About the `example`

 Technical Details[¶](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#technical-details "Permanent link")

### Cookie Parameters
#### How to Use
```python
from typing import Annotated
from fastapi import Cookie, FastAPI
app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
```

### Header Parameters
#### How to Use
```python
from typing import Annotated
from fastapi import FastAPI, Header
app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
```

#### Automatic Conversion

[¶](https://fastapi.tiangolo.com/tutorial/header-params/#automatic-conversion "Permanent link")

emmmm, 会自动把 `-` 变成 `_`

#### Duplicate headers
```python
from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}
```
