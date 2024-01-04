---
title: Rust 错误处理
date: 2023-11-06 01:13
article: false
tags: 
cards-deck: 04 Coding & Tech::01 Programming Language::01 Rust::01 Rust教学

---

一个基本的错误处理案例  
[对返回的错误进行处理](https://course.rs/basic/result-error/result.html#%E5%AF%B9%E8%BF%94%E5%9B%9E%E7%9A%84%E9%94%99%E8%AF%AF%E8%BF%9B%E8%A1%8C%E5%A4%84%E7%90%86)
```rust
use std::fs::File;
use std::io::ErrorKind;
fn main() {
    let f = File::open("hello.txt");
    let f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => panic!("Problem opening the file: {:?}", other_error),
        },
    };
}
```
#card  
[错误处理 - Rust语言圣经(Rust Course)](https://course.rs/advance/errors.html)  
^1699204486030

How to simplify these codes?
```rust
use std::fs::File;
use std::io::{self, Read};
fn read_username_from_file() -> Result<String, io::Error> {
    // 打开文件，f是`Result<文件句柄,io::Error>`
    let f = File::open("hello.txt");
    let mut f = match f {
        // 打开文件成功，将file句柄赋值给f
        Ok(file) => file,
        // 打开文件失败，将错误返回(向上传播)
        Err(e) => return Err(e),
    };
    // 创建动态字符串s
    let mut s = String::new();
    // 从f文件句柄读取数据并写入s中
    match f.read_to_string(&mut s) {
        // 读取成功，返回Ok封装的字符串
        Ok(_) => Ok(s),
        // 将错误向上传播
        Err(e) => Err(e),
    }
}
```
#card  
 [传播界的大明星: ?](https://course.rs/basic/result-error/result.html#%E4%BC%A0%E6%92%AD%E7%95%8C%E7%9A%84%E5%A4%A7%E6%98%8E%E6%98%9F-)
 1. 使用 `？` 来链式传播 Result  
^1699205338958
