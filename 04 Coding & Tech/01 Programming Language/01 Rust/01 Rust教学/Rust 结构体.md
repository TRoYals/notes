---
title: Rust 结构体
date: 2023-10-17 16:14
article: false
tags: 
---

## 相关链接
[结构体的定义和实例化 - Rust 程序设计语言 简体中文版](https://kaisery.github.io/trpl-zh-cn/ch05-01-defining-structs.html)

## Struct 定义及使用
定义一个 struct  
```rust
struct User {  
	active: bool,  
	username: String,  
	email: String,  
	sign_in_count: u64,  
}
```

使用一个定义好的 struct
```rust
fn main() {
    let user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
}
```

在 Rust 中可以使用..来展开一个 struct, 但是记得要放在最后

---
```
在 rust 中  
fn main() {  
	// --snip--

    let user2 = User {
        email: String::from("another@example.com"),
        ..user1
    };
},  
请问这样的 user2 是 clone 的还是 move 的
```

在你给出的 Rust 代码中，`..user1` 是使用了 Rust 的结构体更新语法。这种语法可以用于创建一个新的结构体实例，并从另一实例复制一些或所有字段。

在这种情况下，`user2` 是从 `user1` 中复制了所有未在 `user2` 中明确设置的字段。具体是克隆还是移动取决于字段的类型。对于实现了 `Copy` trait 的类型，如基本数值类型，它们会被复制。对于没有实现 `Copy` trait 的类型，如 `String`，它们会被移动。

在你的示例中，`email` 字段是明确设置的，所以它并未从 `user1` 中移动或复制。其它的字段会从 `user1` 中移动到 `user2`，因为 `String` 类型没有实现 `Copy` trait。这意味着在 `..user1` 之后，`user1` 将不能再被使用，因为它的一部分或全部所有权已经被转移。

如果你希望 `user1` 在此之后仍然可用，你需要对相关字段进行克隆。例如，如果你的 `User` 结构体有一个名为 `username` 的 `String` 字段，你可以这样做：

```rust
let user2 = User {
    email: String::from("another@example.com"),
    username: user1.username.clone(),
    ..user1
};
```

注意，这样做可能会导致编译错误，因为 `..user1` 语法试图移动 `user1` 的所有字段，包括已经被克隆的 `username`。在这种情况下，你可能需要手动为 `user2` 的所有字段赋值，而不是使用 `..user1` 语法。

---

## 元组结构体

[使用没有命名字段的元组结构体来创建不同的类型](https://kaisery.github.io/trpl-zh-cn/ch05-01-defining-structs.html#%E4%BD%BF%E7%94%A8%E6%B2%A1%E6%9C%89%E5%91%BD%E5%90%8D%E5%AD%97%E6%AE%B5%E7%9A%84%E5%85%83%E7%BB%84%E7%BB%93%E6%9E%84%E4%BD%93%E6%9D%A5%E5%88%9B%E5%BB%BA%E4%B8%8D%E5%90%8C%E7%9A%84%E7%B1%BB%E5%9E%8B)

## 没有任何字段的类单元结构体
[没有任何字段的类单元结构体](https://kaisery.github.io/trpl-zh-cn/ch05-01-defining-structs.html#%E6%B2%A1%E6%9C%89%E4%BB%BB%E4%BD%95%E5%AD%97%E6%AE%B5%E7%9A%84%E7%B1%BB%E5%8D%95%E5%85%83%E7%BB%93%E6%9E%84%E4%BD%93)
```rust
struct AlwaysEqual;
fn main() {
    let subject = AlwaysEqual;
}
```
在 [[泛型,Trait和生命周期]] 中会有详细解释

## 结构体数据的所有权
在 `User` 结构体的定义中，我们使用了自身拥有所有权的 `String` 类型而不是 `&str` 字符串 slice 类型。这是一个有意而为之的选择，因为我们想要这个结构体拥有它所有的数据，为此只要整个结构体是有效的话其数据也是有效的。

可以使结构体存储被其他对象拥有的数据的引用，不过这么做的话需要用上 **生命周期**（_lifetimes_），这是一个第十章会讨论的 Rust 功能。生命周期确保结构体引用的数据有效性跟结构体本身保持一致。如果你尝试在结构体中存储一个引用而不指定生命周期将是无效的，比如这样：
```rust
struct User {
    active: bool,
    username: &str,
    email: &str,
    sign_in_count: u64,
}

fn main() {
    let user1 = User {
        active: true,
        username: "someusername123",
        email: "someone@example.com",
        sign_in_count: 1,
    };
}
```

编译器会抱怨它需要生命周期标识符：

```rust
$ cargo run
   Compiling structs v0.1.0 (file:///projects/structs)
error[E0106]: missing lifetime specifier
 --> src/main.rs:3:15
  |
3 |     username: &str,
  |               ^ expected named lifetime parameter
  |
help: consider introducing a named lifetime parameter
  |
1 ~ struct User<'a> {
2 |     active: bool,
3 ~     username: &'a str,
  |

error[E0106]: missing lifetime specifier
 --> src/main.rs:4:12
  |
4 |     email: &str,
  |            ^ expected named lifetime parameter
  |
help: consider introducing a named lifetime parameter
  |
1 ~ struct User<'a> {
2 |     active: bool,
3 |     username: &str,
4 ~     email: &'a str,
  |

For more information about this error, try `rustc --explain E0106`.
error: could not compile `structs` due to 2 previous errors

```

第十章会讲到如何修复这个问题以便在结构体中存储引用，不过现在，我们会使用像 `String` 这类拥有所有权的类型来替代 `&str` 这样的引用以修正这个错误。

ps:  
Q: `&str` 这样的引用拥有所有权吗

A:  
在 Rust 中，`&str` 是一个字符串切片类型，它本质上是一个对某个字符串数据的引用。`&str` 不拥有它所引用的数据的所有权。换言之，当 `&str` 离开其作用域时，它不会负责清理其引用的数据。

这是 Rust 所有权系统的一个核心概念。在 Rust 中，每一块数据都有一个变量作为它的所有者。当所有者离开作用域时，数据将被清理。对于 `&str` 这样的引用，它们只是借用了数据，而不是拥有数据。

例如，如果你有一个 `String` 变量和一个 `&str` 变量，那么 `String` 变量是数据的所有者，而 `&str` 变量只是借用了这个数据。当 `String` 变量离开作用域时，数据将被清理，无论 `&str` 变量是否还在作用域内。

## 结构体示例
```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        area(&rect1)
    );
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}
```

在 Rust 中，函数默认会获取其参数的所有权，除非参数被显式地声明为引用（使用 &）。如果一个函数获取了一个值的所有权，那么在函数结束时，这个值将被丢弃（drop）。这意味着，如果你直接将 `Rectangle` 实例传递给 `area` 函数（即 `area(rectangle: Rectangle)`），那么在 `area` 函数结束时，这个 `Rectangle` 实例将被丢弃，你将无法再次使用它。

然而，如果你将 `Rectangle` 实例的引用（即 `&Rectangle`）传递给 `area` 函数，那么 `area` 函数只会借用这个实例，而不会获取其所有权。这意味着，当 `area` 函数结束时，这个 `Rectangle` 实例不会被丢弃，你可以在函数调用后继续使用它。

所以，在你的例子中，你应该使用 `&Rectangle` 而不是 `Rectangle`，因为你可能希望在调用 `area` 函数后继续使用 `Rectangle` 实例。

## 怎么打印结构体
[通过派生 trait 增加实用功能](https://kaisery.github.io/trpl-zh-cn/ch05-02-example-structs.html#%E9%80%9A%E8%BF%87%E6%B4%BE%E7%94%9F-trait-%E5%A2%9E%E5%8A%A0%E5%AE%9E%E7%94%A8%E5%8A%9F%E8%83%BD)

## 方法语法 (method syntax)
**方法**（method）与函数类似：它们使用 `fn` 关键字和名称声明，可以拥有参数和返回值，同时包含在某处调用该方法时会执行的代码。不过方法与函数是不同的，因为它们在结构体的上下文中被定义（或者是枚举或 trait 对象的上下文，将分别在 [[Rust枚举和模式匹配]] 和 [[Rust 面向对象编程]] 讲解），并且它们第一个参数总是 `self`，它代表调用该方法的结构体实例。

### 定义方法
记一下吧  
```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );
}
```

注意到, 在 rust 中, 不能通过使用 `rect1.width` 的方法来访问 struct, 需要自己定义*getters*来实现这个需求. 通过使用*getters*可以定义私有的字段但是公布公共的方法.

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}
impl Rectangle {
    fn width(&self) -> bool {
        self.width > 0
    }
}
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    if rect1.width() {
        println!("The rectangle has a nonzero width; it is {}", rect1.width);
    }
}
```

## 关联函数
[关联函数](https://kaisery.github.io/trpl-zh-cn/ch05-03-method-syntax.html#%E5%85%B3%E8%81%94%E5%87%BD%E6%95%B0)  
[Rust：函数，方法，关联函数有什么区别？ - 掘金](https://juejin.cn/post/7265944437897838653)

所有在 `impl` 块中定义的函数被称为 **关联函数**（_associated functions_），因为它们与 `impl` 后面命名的类型相关。

关联函数（Associated Function）：关联函数与类型相关联，而不是与类型的实例相关联。它们使用 `impl` 块定义，并使用 `::` 语法调用，例如 `MyStruct::my_associated_function()`。关联函数通常用于创建新的类型实例、提供类型级别的功能或在类型级别上操作数据。

关联函数（在其他语言中也被称为静态方法）是一种不需要实例就能调用的函数。在 Rust 中，你可以在 `impl` 块中定义关联函数。它们的主要优点是提供了一种组织和封装与特定类型相关的功能的方式。

在 Rust 中，关联函数常常被用作**构造函数**。构造函数是一种特殊的方法，用于初始化新创建的对象。在许多面向对象的语言中，构造函数是一个特殊的方法，当你创建一个新的对象时，它会自动被调用。然而，Rust 并不直接支持这种机制，所以通常会使用关联函数来实现类似的功能。

```rust
struct Point {
    x: f64,
    y: f64,
}
impl Point {
    // 关联函数
    fn new(x: f64, y: f64) -> Point {
        Point { x, y }
    }
    // 方法
    fn distance(&self, other: &Point) -> f64 {
        let dx = self.x - other.x;
        let dy = self.y - other.y;
        (dx * dx + dy * dy).sqrt()
    }
}
// 函数
fn print_distance(p1: &Point, p2: &Point) {
    let distance = p1.distance(p2);
    println!("The distance between the points is {}", distance);
}

fn main() {
    let p1 = Point::new(0.0, 0.0);
    let p2 = Point::new(3.0, 4.0);
    print_distance(&p1, &p2);
}

```

## 多个 `impl` 块
可以将方法分配在多个 `impl` 块中, [[泛型,Trait和生命周期]] 中会介绍一些实用的分散 `impl` 块方法.
