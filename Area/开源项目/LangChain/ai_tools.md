---
title: ai_tools

date: 2023-06-18 21:32
article: false
---

## tiktoken

encoding = tiktoken.get_encoding("cl100k_base").encode( text:str)
num: int = len(encoding)

num = len( tiktoken.get_encoding("cl100k_base").encode( text:str))

## ChomeDb
一定要用 TokenTextSplitter!!!! 说多了都是泪
```python
from langchain.text_splitter import CharacterTextSplitter,TokenTextSplitter

with open('../../state_of_the_union.txt') as f:

state_of_the_union = f.read()

text_splitter = TokenTextSplitter(chunk_size=350, chunk_overlap=0,encoding_name="cl100k_base")

texts = text_splitter.split_text(state_of_the_union)

embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_texts(texts, embeddings, metadatas=[{"source": i,"length": len(tiktoken.get_encoding("cl100k_base").encode( texts[i]))} for i in range(len(texts))])
```