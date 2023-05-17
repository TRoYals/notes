---
title: SQL必知必会
date: 2023-05-09 15:31
article: false
star: false
check: 0
---

## 前略

## 检索数据
```ad-tip
如果不明确规定排序顺序，则不应该假定检索出的数据的顺序有任何意义。
```

```mysql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

### order by 多列，默认顺序
在ORDER BY语句中，如果不指定排序顺序，则默认为升序。如果要按多个列排序，可以在ORDER BY子句中指定多个列，并用逗号分隔它们。在这种情况下，MySQL首先按第一个列排序，然后在相同值的情况下按第二个列排序，以此类推。

### order by 排序方式
按照每个字符的ASCII值来排序。
![ASCII Table](https://www.asciitable.com/asciifull.gif)

如果需要不按照大小排序，，可以使用COLLATE关键字来指定排序规则。例如，可以按照不区分大小写的顺序对字符串进行排序，可以使用以下语句：
```sql
SELECT * FROM mytable ORDER BY mycolumn COLLATE utf8_general_ci;
```

## 过滤数据
### where子句
略

### 用通配符
#### Like
%
```
WHERE *** LIKE "%b%"
```

b% 以b/B 开头
%b 以b/B 结尾
%b% 含有B/b

__
待定符
```
WHERE *** LIKE "__b"
```
三个 字符，最后一个字符B结尾

#### REGEXP
```js
where last_name REGEXP "field"
```
"field"  含有 field
"^field" 必须以field开始
"field$" 必须以field结尾
"field|mac" 含有field 或mac
"\[gim\]e" g/i/m + e

## 计算字段
使用 **"+"/Concat/||** 和 **RTRIM** （消除空格） 和 **AS** 来完成数据的组合

##  函数
### 文本处理函数
不同的DBMS支持不同的函数，请按照自己使用的DBMS进行函数的查找
<img src="http://oss.naglfar28.com/naglfar28/202305091752897.png"/>
SOUNDEX 是一个将任何文本串转换为描述其语音表示的字母数字模式的算法。

<img src="http://oss.naglfar28.com/naglfar28/202305091755424.png"/>

SOUNEX()支持： PostgreSQL 不支持，多数 SQLite 实现不支持

### 日期和时间处理函数
因为DBMS的时间函数几乎不相同，抽象一下函数内容：


## 汇总数据
### 聚集函数
在SQL中，聚合函数（Aggregate Functions）用于对数据进行计算和统计，并返回单个值作为结果。
一句话概括：把很多数据聚合成一行
