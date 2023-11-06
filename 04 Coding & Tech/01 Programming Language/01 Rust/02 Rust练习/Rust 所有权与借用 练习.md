---
title: Rust 所有权与借用 练习
date: 2023-10-20 10:07
article: false
tags: 
cards-deck: 04 Coding & Tech::01 Programming Language::01 Rust::02 Rust练习
---

[所有权 - Rust By Practice( Rust 练习实践 )](https://zh.practice.rs/ownership/ownership.html)

## 所有权

从所有权开始
```rust
fn main() {
    // 使用尽可能多的方法来通过编译
    let x = String::from("hello, world");
    let y = x;
    println!("{},{}",x,y);
}
```
#card  
```rust
fn main() {
    let x = String::from("hello, world");
    let y = x.clone();
    println!("{},{}",x,y);
}
```
```rust
fn main() {
    let x = "hello, world";
    let y = x;
    println!("{},{}",x,y);
}
```
```rust
fn main() {
    let x = &String::from("hello, world");
    let y = x;
    println!("{},{}",x,y);
}
```
```rust
fn main() {
    let x = String::from("hello, world");
    let y = x.as_str();
    println!("{},{}",x,y);
}
```
^1697769026075

```rust
// 修复错误，不要删除任何代码行
fn main() {
    let s = String::from("hello, world");
    print_str(&s);
    println!("{}", s);
}
fn print_str(s: String)  {
    println!("{}",s)
}
```
#card
```rust
fn main() {
    let s = String::from("hello, world");
    print_str(s.clone());
    println!("{}", s);
}
fn print_str(s: String)  {
    println!("{}",s)
}```
```rust
 fn main() {
     let s = String::from("hello, world");
     print_str(&s);
     println!("{}", s);
 }
 fn print_str(s: &String)  {
     println!("{}",s)
 }
```
^1697769961902

如果要使用 `str` 类型，只能配合 `Box`。 `&` 可以用来将 `Box<str>` 转换为 `&str` 类型
```rust
// 使用至少两种方法来修复错误
fn main() {
    let s: Box<str> = "hello, world".into();
    greetings(s)
}
eetings(s: &str) {
    println!("{}",s)
}
```
#card  
细品!
```rust
fn main() {
    let s: Box<str> = "hello, world".into();
    greetings(&s)
}
fn greetings(s: &str) {
    println!("{}",s)
}
```
```rust
fn main() {
    let s: Box<&str> = "hello, world".into();
    greetings(*s)
}
fn greetings(s: &str) {
    println!("{}",s)
}
```
```rust
fn main() {
    let s: Box<str> = "hello, world".into();
    greetings(&*s)
}
fn greetings(s: &str) {
    println!("{}",s)
}
```
^1697780323832


// 修复所有错误，不要删除任何一行代码
```rust
fn main() {
    let s1 = String::from("hello,");
    let s2 = String::from("world!");
    let s3 = s1 + s2; 
    assert_eq!(s3,"hello,world!");
    println!("{}",s1);
}
```
#card 
```rust
fn main() {
    let s1 = String::from("hello,");
    let s2 = String::from("world!");
    let s3 = s1.clone() + s2.as_str(); 
    assert_eq!(s3,"hello,world!");
    println!("{}",s1);
}
```
首先，要理解为什么原始代码有问题：在 Rust 中，使用 `+` 运算符将两个 `String` 对象相加实际上是调用了 `String` 的 `add` 方法，这样的操作会消耗（即移动）左侧的 `String`，使其在后续不再可用。因此，在原始代码中，`s1` 在与 `s2` 相加后被移动了，所以不能再次使用。  
您的修复方法是克隆 `s1` 以避免移动它，这是正确的。但还有另一种常用的方法来连接两个字符串，那就是使用 `format!` 宏，它不会移动任何字符串：
``` rust
fn main() {
    let s1 = String::from("hello,");
    let s2 = String::from("world!");
    let s3 = format!("{}{}", s1, s2); 
    assert_eq!(s3, "hello,world!");
    println!("{}", s1);
}
```
^1697781557920

