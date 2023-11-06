---
title: Rust 流程控制
date: 2023-10-20 14:48
article: false
tags: 
---

## 循环控制
### for 循环
```rust
fn main() {
    for i in 1..=5 {
        println!("{}", i);
    }
}
```
使用 for 的时候, 往往使用集合的引用形式.

| 使用方法                      | 等价使用方式                                      | 所有权     |
| ----------------------------- | ------------------------------------------------- | ---------- |
| `for item in collection`      | `for item in IntoIterator::into_iter(collection)` | 转移所有权 |
| `for item in &collection`     | `for item in collection.iter()`                   | 不可变借用 |
| `for item in &mut collection` | `for item in collection.iter_mut()`               | 可变借用   |

在循环中获取元素的索引
```
fn main() {
    let a = [4, 3, 2, 1];
    // `.iter()` 方法把 `a` 数组变成一个迭代器
    for (i, v) in a.iter().enumerate() {
        println!("第{}个元素是{}", i + 1, v);
    }
}
```
