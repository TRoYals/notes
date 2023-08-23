---
title: sqlalchemy 基础介绍
date: 2023-08-15 10:22
article: false
tags: 
---

# 相关资源

[SQLAlchemy Unified Tutorial — SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/tutorial/index.html)

# Connection
## engine.connect()

使用 with statement(python Context manager form), 来进行链接

```python
from sqlalchemy import text
with engine.connect() as conn:
	result = conn.execute(text("select 'hello world'"))
	print(result.all())
```

在这样的情形下, 虽然 会关闭链接, 但不会 commit 内容  
需要通过, conn.commit() 来提交内容更改

