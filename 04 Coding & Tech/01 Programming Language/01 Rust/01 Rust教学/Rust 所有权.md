---
title: Rust 所有权相关
date: 2023-10-12 17:04
article: false
tags:
cards-deck: 04 Coding & Tech::01 Programming Language::01 Rust::01 Rust教学
---

## Rust 所有权规则 #card 
1. Rust 中的每一个值都有一个 **所有者**（_owner_）。
2. 值在任一时刻有且只有一个所有者。
3. 当所有者（变量）离开作用域，这个值将被丢弃。

## 导入
### 从字符串字面值和 String 说起

字符串字面值（string literals）是指由双引号括起来的文本字符串。例如:  
`let greeting = "Hello, World!";

`string` 中使用 ` let mut s = String::from("hello");` 可以使用字符串类型. 对于 `String` 类型，为了支持一个可变，可增长的文本片段，需要在堆上分配一块在编译时未知大小的内存来存放内容。这意味着：

- 必须在运行时向内存分配器（memory allocator）请求内存。
- 需要一个当我们处理完 `String` 时将内存返回给分配器的方法。

Rust 中处理内存的策略:

> 内存在拥有它的变量离开作用域后就被自动释放。

## 变量与数据交互的方式

### 移动

二次污染 (double free) #card 
```
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;
}
```
<br>
![image.png](http://oss.naglfar28.com/naglfar28/202310121739203.png)  
s1 和 s2 指向同一个位置.  
当 s2 和 s1 离开作用域后, 他们会释放相同的内存. 这是一个叫做**二次释放**的问题, 两次释放同一个内存会导致内存污染.
^1697705718366

为了解决这个问题, 当在 rust 中使用栈复制时, 原理的那个会被移动掉. 简单来说

```rust
let s1 = String::from("hello"); 
let s2 = s1; 
println!("{}, world!", s1);
```

这样会报错!

这样就把 " 二次释放 " 的问题解决了.

### 克隆

这样可以解决这个问题了, 同过使用 clone

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1.clone();

    println!("s1 = {}, s2 = {}", s1, s2);
}

```

Rust 有一个叫做 [[Copy trait]] 的特殊注解, 可以用在类似整型这样的<存储在栈上的类型>上. 如果一个类型实现了 `Copy` trait，那么一个旧的变量在将其赋值给其他变量后仍然可用。

## 所有权与函数

多读几遍!  
将值传递给函数与给变量赋值的原理相似。向函数传递值可能会移动或者复制，就像赋值语句一样。

```
fn main() {
    let s = String::from("hello");  // s 进入作用域

    takes_ownership(s);             // s 的值移动到函数里 ...
                                    // ... 所以到这里不再有效

    let x = 5;                      // x 进入作用域

    makes_copy(x);                  // x 应该移动函数里，
                                    // 但 i32 是 Copy 的，
                                    // 所以在后面可继续使用 x

} // 这里，x 先移出了作用域，然后是 s。但因为 s 的值已被移走，
  // 没有特殊之处

fn takes_ownership(some_string: String) { // some_string 进入作用域
    println!("{}", some_string);
} // 这里，some_string 移出作用域并调用 `drop` 方法。
  // 占用的内存被释放

fn makes_copy(some_integer: i32) { // some_integer 进入作用域
    println!("{}", some_integer);
} // 这里，some_integer 移出作用域。没有特殊之处
```

## Copy 属性
Rust 有一个叫做 `Copy` 的特征，可以用在类似整型这样在栈中存储的类型。如果一个类型拥有 `Copy` 特征，一个旧的变量在被赋值给其他变量后仍然可用。  
那么什么类型是可 `Copy` 的呢？可以查看给定类型的文档来确认，不过作为一个通用的规则： **任何基本类型的组合可以 `Copy` ，不需要分配内存或某种形式资源的类型是可以 `Copy` 的**。如下是一些 `Copy` 的类型：  
#card 
- 所有整数类型，比如 `u32`
- 布尔类型，`bool`，它的值是 `true` 和 `false`
- 所有浮点数类型，比如 `f64`
- 字符类型，`char`
- 元组，当且仅当其包含的类型也都是 `Copy` 的时候。比如，`(i32, i32)` 是 `Copy` 的，但 `(i32, String)` 就不是
- 不可变引用 `&T` ，例如 [转移所有权](https://course.rs/basic/ownership/ownership.html#%E8%BD%AC%E7%A7%BB%E6%89%80%E6%9C%89%E6%9D%83) 中的最后一个例子，**但是注意: 可变引用 `&mut T` 是不可以 Copy 的**  
^1697705718373

[函数传值与返回](https://course.rs/basic/ownership/ownership.html#%E5%87%BD%E6%95%B0%E4%BC%A0%E5%80%BC%E4%B8%8E%E8%BF%94%E5%9B%9E)
