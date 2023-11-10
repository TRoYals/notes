---
title: Comprehensive Rust
date: 2023-11-07 15:38
article: false
tags: 
cards-deck: 04 Coding & Tech::01 Programming Language::01 Rust::01 Rust教学
---

# Day1
## why Rust
[An Example in C - Comprehensive Rust 🦀](https://google.github.io/comprehensive-rust/why-rust/an-example-in-c.html)

### Runtime Graratees
How to create memory leak in Rust  
[Compile Time Guarantees - Comprehensive Rust 🦀](https://google.github.io/comprehensive-rust/why-rust/compile-time.html)

why we need it?
```ad-info
Rust is designed with the goal of safe memory management, and its ownership system typically ensures that memory is automatically cleaned up when it's no longer in use. However, Rust does allow memory leaks because:

1. **Flexibility and Control**: Rust provides low-level control over memory, which can be necessary for certain use cases where the programmer wants to manage memory themselves for the sake of optimization or interfacing with other languages or systems.

2. **Runtime-initialized Statics**: As you mentioned, `Box::leak` can be used to create static variables that are initialized at runtime. This is useful for cases where you need a `'static` lifetime but you can't or don't want to initialize the data at compile time.

3. **Preventing Destructors**: The `std::mem::forget` function allows you to prevent a value's destructor from running. This can be useful when the destructor has side effects that you explicitly want to avoid or when transferring ownership of the underlying resource to other code (such as FFI with other programming languages).

4. **Reference Cycles**: While not an intentional feature, the ability to create reference cycles (for example with `Rc` or `Arc`) is a side effect of providing reference-counted pointers that can be used to build complex data structures, like graphs. Handling reference cycles would require a garbage collector, which Rust opts out of in favor of compile-time checks, with the understanding that the programmer must ensure that cycles are broken manually if they do occur.

5. **Endless Collections**: Rust does not stop you from continually adding to a collection such as a `Vec` or `HashMap`, which can grow until the system runs out of memory. This is intentional, as limiting this would be too restrictive and would prevent legitimate use cases where the program might need to consume a lot of memory.

6. **Interfacing with System-Level Details**: Certain OS-level details or specific libraries may require that an object's memory outlives its scope within Rust, and this might lead to deliberate memory "leakage" from Rust's perspective, though the system or the library knows how to handle this memory.

In summary, while Rust's strong ownership and borrowing semantics do a great deal to prevent memory leaks, complete prevention of memory leaks is impractical and would limit the language's power and flexibility. By allowing controlled memory leaks, Rust gives programmers the tools they need to manage memory in the way that they decide is best for their particular situation, without compromising the overall safety guarantees of the language.
```

How to close the array bounds check and the integer overflow check?  
[Runtime Guarantees - Comprehensive Rust 🦀](https://google.github.io/comprehensive-rust/why-rust/runtime.html)

### Modern Features
#### [Language Features](https://google.github.io/comprehensive-rust/why-rust/modern.html#language-features)

- Enums and pattern matching.
- Generics.(泛型)
- No overhead FFI(Foreign Function Interface). ps.need `unsafe`
- Zero-cost abstractions.

#### [Tooling](https://google.github.io/comprehensive-rust/why-rust/modern.html#tooling)

- Great compiler errors.
- Built-in dependency manager.
- Built-in support for testing.
- Excellent Language Server Protocol support.

### Docs
[Docs.rs](https://docs.rs/)

[What is rustdoc? - The rustdoc book](https://doc.rust-lang.org/rustdoc/what-is-rustdoc.html)

## exercise
[Implicit Conversions](https://google.github.io/comprehensive-rust/exercises/day-1/implicit-conversions.html#implicit-conversions)
```rust
fn multiply(x: i32, y: i32) -> i16 {
    (x * y).into()
}
fn main() {
    let x: i8 = 15;
    let y: i16 = 10;
    println!("{x} * {y} = {}", multiply(x.into(), y.into()));
}
```
这个代码会报什么错  
#card 
1. i32 不能转换为 i16, 可以用 `as` 来进行一个简单截断, 但这样明显不好
2. 使用 `checked_mul` 来检查是否溢出
```rust
fn multiply(x: i32, y: i32) -> i16 {
    x.checked_mul(y)
     .expect("Overflow occurred")
     .try_into()
     .expect("Conversion to i16 failed")
}
```
3.使用 `try_into()`
```rust
use std::convert::TryInto;
fn multiply(x: i32, y: i32) -> i16 {
    let result: i32 = x * y;
    result.try_into().unwrap_or_else(|_| panic!("Overflow occurred"))
}
```
^1699349133788

[Arrays and for Loops](https://google.github.io/comprehensive-rust/exercises/day-1/for-loops.html#arrays-and-for-loops)
