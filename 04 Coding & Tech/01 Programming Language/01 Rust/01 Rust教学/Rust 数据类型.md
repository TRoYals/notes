---
title: Rust 数据类型
date: 2023-10-11 14:26
article: false
tags:
---

## Rust 数据类型
### 标量类型 (scalar)
#### 整型

[数据类型 - Rust 程序设计语言 简体中文版](https://kaisery.github.io/trpl-zh-cn/ch03-02-data-types.html)

每一个有符号的变体可以储存包含从 $-(2^{n-1})$ 到 $2^{n-1}-1$ 在内的数字，这里 _n_ 是变体使用的位数。所以 `i8` 可以储存从 $-2^7$ 到 $2^7-1$ 在内的数字，也就是从 -128 到 127。无符号的变体可以储存从 0 到 $2^{n-1}$ 的数字，所以 `u8` 可以储存从 0 到 $2^8-1$ 的数字，也就是从 0 到 255。

那么该使用哪种类型的数字呢？如果拿不定主意，Rust 的默认类型通常是个不错的起点，数字类型默认是 `i32`。`isize` 或 `usize` 主要作为某些集合的索引

> 用 i32 作为默认的数字看起来不错

可能会遇到整型溢出的问题  
[整型溢出](https://kaisery.github.io/trpl-zh-cn/ch03-02-data-types.html#%E6%95%B4%E5%9E%8B%E6%BA%A2%E5%87%BA)

#### 浮点数

rust 默认浮点数是 `f64`, 浮点数都是有符号的.  
浮点数采用 [IEEE 754](https://zh.wikipedia.org/zh-sg/IEEE_754) 标准表示。`f32` 是单精度浮点数，`f64` 是双精度浮点数。

#### 数值运算

`+ - * / %`

#### 字符类型

用单引号\' 声明 `char` 字面量, 用 双引号声明 字符串字面量. 

#### 复合类型
##### 元组
```
fn main() { 
let tup: (i32, f64, u8) = (500, 6.4, 1); 
}
```
也可以这么使用元组
```
fn main() { 
let x: (i32, f64, u8) = (500, 6.4, 1); 
let five_hundred = x.0; 
let six_point_four = x.1; 
let one = x.2; 
}
``` 
##### 数字
```
let a: [i32; 5] = [1, 2, 3, 4, 5];
let a = [3;5];
```

### slice 类型
[rust语言基础学习: rust中的slice类型 | 青蛙小白](https://blog.frognew.com/2020/07/rust-slice-types.html)  
ps: **字符串字面量就是 slice 类型**
#### 为什么需要
对于常用的集合类型例如 `Vec<T>`, `String`(String 的底层是 `Vec<u8>`)，这些集合类型的引用类型 `&Vec<T>`, `&String`，引用的将是整个集合的内容。

在一些特定的场景中，我们需要只引用集合中一段连续的元素序列，而不是引用整个集合的内容。 **因此 Rust 提供了一类 slice 类型，使用 slice 类型可以只引用集合中一部分连续的元素。**

例如有一个集合变量 `x`，则创建一个基于 x 的 slice 的语法是 `&x[start_index..end_index]`，注意创建的 slice 是以 " 借用 " 形式存在，所以在 x 前面加了引用操作符 `&`。