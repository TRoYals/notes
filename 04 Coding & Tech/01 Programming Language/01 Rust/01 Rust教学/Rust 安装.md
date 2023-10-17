---
title: Rust 安装
date: 2023-10-06 17:38
article: false
tags:
---
## Rust 安装

[Installation - The Rust Programming Language](https://rust-book.cs.brown.edu/ch01-01-installation.html)  
使用 **RustUp** 管理 Rust 版本

```text
**Rust is installed now. Great!**
To get started you may need to restart your current shell.
This would reload your **PATH** environment variable to include
Cargo's bin directory ($HOME/.cargo/bin).

```

linker 是什么?

```
You will also need a _linker_, which is a program that Rust uses to join its compiled outputs into one file. It is likely you already have one. If you get linker errors, you should install a C compiler, which will typically include a linker. A C compiler is also useful because some common Rust packages depend on C code and will need a C compiler.
```

## hello world! 
```rust
fn main() { 
    println!("Hello, world!"); 
}
```

[Hello, World! - Rust 程序设计语言 简体中文版](https://kaisery.github.io/trpl-zh-cn/ch01-02-hello-world.html)  
 Rust 的缩进风格使用 **4 个空格**，而不是 1 个制表符（tab）。

 `println!` 调用了一个 Rust 宏（macro）。如果是调用函数，则应输入 `println`（没有 `!`）。我们将在第十九章详细讨论宏。现在你只需记住，当看到符号 `!` 的时候，就意味着调用的是宏而不是普通函数，并且宏并不总是遵循与函数相同的规则
