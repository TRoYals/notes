---
title: Rust 模式匹配流程控制 练习
date: 2023-10-26 10:13
article: false
tags: 
cards-deck: 04 Coding & Tech::01 Programming Language::01 Rust::02 Rust练习
---

🌟🌟 使用模式 `&mut V` 去匹配一个可变引用时，你需要格外小心，因为匹配出来的 `V` 是一个值，而不是可变引用 
```rust
// 修复错误，尽量少地修改代码
// 不要移除任何代码行
fn main() {
    let mut v = String::from("hello,");
    let r = &mut v;
    match r {
       &mut value => value.push_str(" world!") 
    }
}
```
#card 
```rust
fn main() {
    let mut v = String::from("hello,");
    let r = &mut v;
    match r {
       value => value.push_str(" world!") 
    }
}
```
^1698286460897

```rust
fn main() {
    let a = [4,3,2,1];
    // 通过索引和值的方式迭代数组 `a` 
    for (i,v) in a.__ {
        println!("第{}个元素是{}",i+1,v);
    }
}
```
#card 
```rust
fn main() {
    let a = [4,3,2,1];
    // 通过索引和值的方式迭代数组 `a` 
    for (i,v) in a.iter().enumerate() {
        println!("第{}个元素是{}",i+1,v);
    }
}
```
^1698805766918

🌟🌟🌟 当有多层循环时，你可以使用 `continue` 或 `break` 来控制外层的循环。要实现这一点，外部的循环必须拥有一个标签 `'label`, 然后在 `break` 或 `continue` 时指定该标签
```rust
fn main() {
    let mut count = 0;
    'outer: loop {
        'inner1: loop {
            if count >= 20 {
                // 这只会跳出 inner1 循环
                break 'inner1; // 这里使用 `break` 也是一样的
            }
            count += 2;
        }
        count += 5;
        'inner2: loop {
            if count >= 30 {
                break 'outer;
            }
            continue 'outer;
        }
    }
    assert!(count == __)
}
```
#card  
30  
^1698805766923

```rust
fn main() {
    let alphabets = ['a', 'E', 'Z', '0', 'x', '9' , 'Y'];
    // 使用 `matches` 填空
    for ab in alphabets {
        assert!(__)
    }
} 
```
#card 
```rust
fn main() {
    let alphabets = ['a', 'E', 'Z', '0', 'x', '9' , 'Y'];
    // fill the blank with `matches!` to make the code work
    for ab in alphabets {
        assert!(matches!(ab, 'a'..='z' | 'A'..='Z' | '0'..='9'))
    }
} 
```

```rust
enum MyEnum {
    Foo,
    Bar
}
fn main() {
    let mut count = 0;
    let v = vec![MyEnum::Foo,MyEnum::Bar,MyEnum::Foo];
    for e in v {
        if e == MyEnum::Foo { // 修复错误，只能修改本行代码
            count += 1;
        }
    }
    assert_eq!(count, 2);
}
```
#card 
```rust
enum MyEnum {
    Foo,
    Bar
}
fn main() {
    let mut count = 0;
    let v = vec![MyEnum::Foo,MyEnum::Bar,MyEnum::Foo];
    for e in v {
        if matches!(e , MyEnum::Foo) { // fix the error with changing only this line
            count += 1;
        }
    }
    assert_eq!(count, 2);
}
```
也可以这样  
` if let MyEnum::Foo = e{ // 修复错误，只能修改本行代码  

Shadowing
```rust
// 就地修复错误
fn main() {
    let age = Some(30);
    if let Some(age) = age { // 创建一个新的变量，该变量与之前的 `age` 变量同名
       assert_eq!(age, Some(30));
    } // 新的 `age` 变量在这里超出作用域
    match age {
        // `match` 也能实现变量遮蔽
        Some(age) =>  println!("age 是一个新的变量，它的值是 {}",age),
        _ => ()
    }
 }
```
#card 
```rust
    let age = Some(30);
    if let Some(age) = age { // 创建一个新的变量，该变量与之前的 `age` 变量同名
       assert_eq!(age, 30);
    } // 新的 `age` 变量在这里超出作用域
```

🌟🌟🌟 `@` 操作符可以让我们将一个与模式相匹配的值绑定到新的变量上
```rust
struct Point {
    x: i32,
    y: i32,
}
fn main() {
    // 填空，让 p 匹配第二个分支
    let p = Point { x: __, y: __ };
    match p {
        Point { x, y: 0 } => println!("On the x axis at {}", x),
        // 第二个分支
        Point { x: 0..=5, y: y@ (10 | 20 | 30) } => println!("On the y axis at {}", y),
        Point { x, y } => println!("On neither axis: ({}, {})", x, y),
    }
}
```
#card  
在 Rust 中，`@` 操作符用于模式匹配中，允许你同时进行模式匹配和值绑定。这意味着你可以检查值是否符合某个模式，并且在匹配时同时捕获该值并将其绑定到一个新的变量。  
这是一个简单的示例来解释这个概念：
```rust
fn main() {
    let some_value = Some(5);

    match some_value {
        Some(x) if x > 3 => println!("value is greater than 3, and x is {}", x),
        Some(x @ 1..=3) => println!("value is between 1 and 3, inclusive, and x is {}", x),
        Some(x) => println!("value is some other number, and x is {}", x),
        None => println!("value is None"),
    }
}
```
在上述代码中，我们使用了 `x @ 1..=3` 这样的模式匹配。这表示：如果 `some_value` 是一个在 1 到 3 之间的数（包括 1 和 3），我们不仅仅知道它匹配这个模式，还可以通过变量 `x` 来访问这个值。
