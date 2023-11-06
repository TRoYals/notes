---
title: Rust 枚举和模式匹配
date: 2023-10-17 17:52
article: false
tags: 
---
枚举 (*enumerations*), 简称 *enums*.  
枚举允许你通过列举可能的**成员**(*variants*) 来定义一个类型.

## 为什么要有枚举
在 Rust 中，枚举（enum）是一种数据类型，它允许你创建一种新的类型，这种类型可以包含多种不同的值。每个值都可以有不同的数据类型和/或数量。这是一种非常强大的功能，因为它允许你在一个单一的数据类型中封装多种不同的值和类型。这种功能在许多编程语言中都没有，包括 Python。

例如，你可能想要创建一个表示网络状态的枚举。在 Rust 中，你可以这样做：

```rust
enum NetworkStatus {
    Connected,
    Disconnected,
    Connecting { percentage: u32 },
}
```

在这个枚举中，`Connected` 和 `Disconnected` 是无数据的变体，而 `Connecting` 是一个带有数据的变体。这个数据是一个表示连接进度的百分比。

在 Python 中，你可能需要使用类来模拟这种行为，因为 Python 没有内置的枚举类型：

```python
class NetworkStatus:
    def __init__(self, status, percentage=None):
        self.status = status
        self.percentage = percentage
```

然后，你可以像这样创建一个 `NetworkStatus` 对象：

```python
status = NetworkStatus('Connecting', percentage=50)
```

但是，这种方法不如 Rust 的枚举直观。在 Rust 的枚举中，你可以清楚地看到 `NetworkStatus` 可以有哪些值，以及每个值可能带有的数据。在 Python 的例子中，你需要查看 `NetworkStatus` 类的实现，才能了解它可以有哪些值和数据。

此外，Rust 的枚举还有一个重要的优点，那就是它们可以在编译时进行模式匹配。这意味着你可以写出非常强大的代码，而编译器会确保你处理了所有可能的情况。这是 Python 所没有的功能，因为 Python 是一种动态类型的语言。

总的来说，Rust 的枚举是一种非常强大的功能，它们提供了一种在一个数据类型中封装多种不同值和类型的方法。尽管 Python 没有内置的枚举类型，但你可以使用类来模拟相似的行为。

## option\<T\>

```rust
enum Option<T> {
    None,
    Some(T),
}
```

`  <T>` 语法是一个我们还未讲到的 Rust 功能。它是一个泛型类型参数，[[泛型,Trait和生命周期]] 中会更详细的讲解泛型。目前，所有你需要知道的就是 `<T>` 意味着 `Option` 枚举的 `Some` 成员可以包含任意类型的数据，同时每一个用于 `T` 位置的具体类型使得 `Option<T>` 整体作为不同的类型。

[Option in std::option - Rust](https://doc.rust-lang.org/std/option/enum.Option.html)

只要一个值不是 `Option<T>` 类型，你就 **可以** 安全的认定它的值不为空。

## match 控制流程
[match 控制流结构](https://kaisery.github.io/trpl-zh-cn/ch06-02-match.html#match-%E6%8E%A7%E5%88%B6%E6%B5%81%E7%BB%93%E6%9E%84)  

Rust 有一个叫做 `match` 的极为强大的**控制流运算符**，它允许我们将一个值与一系列的模式相比较，并根据相匹配的模式执行相应代码。模式可由字面值、变量、通配符和许多其他内容构成；[第十八章](https://kaisery.github.io/trpl-zh-cn/ch18-00-patterns.html) 会涉及到所有不同种类的模式以及它们的作用。`match` 的力量来源于模式的表现力以及编译器检查，它确保了所有可能的情况都得到处理。

## if let 匹配
[if let 匹配](https://course.rs/basic/match-pattern/match-if-let.html#if-let-%E5%8C%B9%E9%85%8D)  
这两种匹配对于新手来说，可能有些难以抉择，但是只要记住一点就好：**当你只要匹配一个条件，且忽略其他条件时就用 `if let` ，否则都用 `match`**。