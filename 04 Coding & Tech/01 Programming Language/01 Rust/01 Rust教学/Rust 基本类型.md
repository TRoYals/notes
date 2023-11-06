---
title: Rust 基本类型
date: 2023-10-19 14:54
article: false
tags: 
---
## 数值类型
[数值类型 - Rust语言圣经(Rust Course)](https://course.rs/basic/base-type/numbers.html)
## 整数类型
每个有符号类型规定的数字范围是 -(2n - 1) ~ 2n - 1 - 1，其中 `n` 是该定义形式的位长度。因此 `i8` 可存储数字范围是 -(27) ~ 27 - 1，即 -128 ~ 127。无符号类型可以存储的数字范围是 0 ~ 2n - 1，所以 `u8` 能够存储的数字为 0 ~ 28 - 1，即 0 ~ 255。

i: integer 缩写, u: unsigned 缩写  
Rust 整型默认使用 `i32`
### 浮点类型
[浮点类型](https://course.rs/basic/base-type/numbers.html#%E6%B5%AE%E7%82%B9%E7%B1%BB%E5%9E%8B)
#### 浮点数陷阱
1. 浮点数对比
#### NaN (NaN 是浮点数)
**所有跟 `NaN` 交互的操作，都会返回一个 `NaN`**，而且 `NaN` 不能用来比较

