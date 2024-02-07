---
title: JavaScript Cheet Sheet
date: 2024-02-07 16:30
article: false
tags: 
cards-deck: 04 Coding & Tech::01 Programming Language::04 JavaScript
---

## 字符串操作
### 编码相关
charCodeAt codePointAt  
有点像 rust 中的字符操作, 不解释了
```javascript
let char = '𠮷';
console.log(char.charCodeAt(0)); // 输出: 55362
console.log(char.codePointAt(0)); // 输出: 134071
```

## 数组操作
迅速构建一个数组
```javascript
let a = Array.from({length:26},(x,_)=>0)//
let a = Array.from({length:26},(x,index)=>index)//构造一个0-25数组
```

## 字典操作
字典和数组结合 (如何给字典 index 属性) #card  
看这道 mid-451, 我觉得很合适 
```javascript
var frequencySort = function (s) {
  let hashMap = {};
  [...s].forEach((char) => {
    if (hashMap[char]) {
      hashMap[char]++;
    } else {
      hashMap[char] = 1;
    }
  });
  let arr = Object.entries(hashMap);
  arr.sort((a, b) => b[1] - a[1]);
  let result = arr.map(([char, freq]) => char.repeat(freq)).join("");
  return result;
};
```
^1707295905874

## 循环操作
### 循环字符串
1. 普通 for 循环
```javascript
for(let i = 0;i<s.length;i++)
```
2. for... of 循环
```javascript
for (const char of s){}
```
3. Array.prototype.forEach 循环  
**注意!!!!!!**  
forEach 中的 return 只会退出当前步骤!!!!,  
如果需要返回判断的话不要使用 forEach
```javascript
Array.from(str).forEach(char => console.log(char));
[...str].forEach(char => console.log(char));
```
