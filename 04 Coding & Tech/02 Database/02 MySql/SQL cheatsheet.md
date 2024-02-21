---
title: SQL cheatsheet
date: 2024-02-19 13:08
article: false
tags: 
---

## select 操作

### select 执行顺序
1. **FROM** 子句：确定要从哪个表中选择数据。
2. **WHERE** 子句：基于指定的条件过滤数据。
3. **GROUP BY** 子句：将数据分组。
4. **HAVING** 子句：过滤分组后的数据。
5. **SELECT** 子句：选择从数据中返回哪些列或表达式。
6. **ORDER BY** 子句：对结果集进行排序。
7. **LIMIT** / **OFFSET** 子句：限制返回的数据数量。

### select 注意事项
1. group by 在 order by 之前使用, 可以理解为 order by 是 return 里的一个依赖注入  

怎么顺序打印  
`Order by <name> desc/asc'

怎么去重
## Join
### select Join
[SQL | Join (Inner, Left, Right and Full Joins) - GeeksforGeeks](https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/)
### cross join
[1280. 学生们参加各科测试的次数 - 力扣（LeetCode）](https://leetcode.cn/problems/students-and-examinations/description/?envType=study-plan-v2&envId=sql-free-50)

## sql 常见函数
`length`: 取长度  
`datediff()`: 取日期差  
`if`:  
	`ROUND(SUM(IF(sign.action='confirmed',1,0))/count(*),2) AS confirmation_rate,`
