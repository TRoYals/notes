---
title: Rust 复合类型 练习
date: 2023-10-20 14:23
article: false
tags: 
cards-deck: 04 Coding & Tech::01 Programming Language::01 Rust::02 Rust练习
---

```rust
// 修复所有错误
fn main() {
    let mut s = String::from("hello world");
    // 这里, &s 是 `&String` 类型，但是 `first_character` 函数需要的是 `&str` 类型。
    // 尽管两个类型不一样，但是代码仍然可以工作，原因是 `&String` 会被隐式地转换成 `&str` 类型，如果大家想要知道更多，可以看看 Deref 章节: https://course.rs/advance/smart-pointer/deref.html
    let ch = first_character(&s);
    s.clear(); // error!
    println!("the first character is: {}", ch);
}
fn first_character(s: &str) -> &str {
    &s[..1]
}
```
#card 
```rust
fn main() {
    let mut s = String::from("hello world");
    // here, &s is `&String` type, but `first_word` need a `&str` type.
    // it works because `&String` can be implicitly converted to `&str, If you want know more ,this is called `Deref` 
    let word = first_word(&s);
    println!("the first word is: {}", word);
    s.clear();
}
fn first_word(s: &str) -> &str {
    &s[..1]
}
```
^1697784313055
