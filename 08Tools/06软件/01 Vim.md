---
title: Vim
date: 2023-08-08 15:46
article: false
tags: 
---

## 背景资料

[简明 Vim 练级攻略 | 酷 壳 - CoolShell](https://coolshell.cn/articles/5426.html)

## 
### G 相关 (行移动定位)

normal 模式下:  
`ctrl`+`g` 显示文件行数信息  
`G` 返回文件底  
`gg` 返回文件头

## 搜索 (`/`)

在 normal 模式下  
按 `/` 输入要查找的内容然后按 `<enter>`  
输入 `n` 搜寻下个, 输入 `N` 搜寻上个

## 定位与返回 (`ctrl`+`O`/`I`)

`ctrl`+`O` 返回上个搜索的定位处?  
`ctrl`+`I` 返回下个定位处?  
感觉没有说太清楚, 但是有点像 marginnote 的那个跳转.

## 全文替换

To change every occurrence of a character string between two lines,

     type  :#,#s/old/new/g    where #,# are the line numbers of the range

                               of lines where the substitution is to be done.

     Type  :%s/old/new/g      to change every occurrence in the whole file.

     Type  :%s/old/new/gc     to find every occurrence in the whole file,

                               with a prompt whether to substitute or not.

     要更改两行间的所有的匹配字符串：  
     type  :#,#s/old/new/g    其中，#,#是要更改的行号的范围

     Type  :%s/old/new/g      更改全文件中的所有事件。

## 