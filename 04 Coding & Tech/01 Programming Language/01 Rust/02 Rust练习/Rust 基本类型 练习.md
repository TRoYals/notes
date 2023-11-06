---
title: Rust 基本类型 练习
date: 2023-10-19 15:17
article: false
tags: 
cards-deck: 04 Coding & Tech::01 Programming Language::01 Rust::02 Rust练习
---

## 浮点数
使用两种方法来让下面代码工作
```rust
fn main() {
    assert!(0.1+0.2==0.3);
}
```
#card 
```rust
fn main() {
    assert!(0.1_f32+0.2_f3
2==0.3_f32);
}
fn main() {
    assert!((0.1_f64+ 0.2 - 0.3).abs() < 0.001);
}
```
^1697703704328

## 函数
用两种方法求解
```rust
fn main() {
    never_return();
}

fn never_return() -> ! {
    // 实现这个函数，不要修改函数签名!
    
}
```
#card 
```rust
fn main() {
    never_return();
}

fn never_return() -> ! {
    // implement this function, don't modify fn signatures
    panic!("I return nothing!")
}
```
```rust
fn main() {
    never_return();
}

use std::thread;
use std::time;

fn never_return() -> ! {
    // implement this function, don't modify fn signatures
    loop {
        println!("I return nothing");
        // sleeping for 1 second to avoid exhausting the cpu resource
        thread::sleep(time::Duration::from_secs(1))
    }
}
```