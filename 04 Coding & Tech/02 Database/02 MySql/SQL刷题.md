---
title: SQL练习
date: 2024-02-19 13:04
article: false
tags: 
cards-deck: 04 Coding & Tech::02 Database::02 MySql
---

[sql top50](https://leetcode.com/studyplan/top-sql-50/)  
[[SQL cheatsheet]]

### 1280
cross join 和嵌套 join 一定要掌握  
[1280. 学生们参加各科测试的次数 - 力扣（LeetCode）](https://leetcode.cn/problems/students-and-examinations/description/?envType=study-plan-v2&envId=sql-free-50) #card 
```mysql
select s.student_id,student_name,sub.subject_name,IFNULL(count_exams.attended_exams,0) as attended_exams
from Students as s
cross join Subjects as sub
left join (
select student_id,subject_name,count(*) as attended_exams
from Examinations
group by student_id,subject_name
) count_exams
on s.student_id = count_exams.student_id and sub.subject_name = count_exams.subject_name
group by s.student_id, sub.subject_name
order by s.student_id,sub.subject_name
```
^1708497968093
