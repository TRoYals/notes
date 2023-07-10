---
doc_type: hypothesis-highlights
url: >-
  https://jrsinclair.com/articles/2019/algebraic-structures-what-i-wish-someone-had-explained-about-functional-programming
---

# Algebraic Structures: Things I wish someone had explained about functional programming

## Metadata
- Author: [jrsinclair.com]()
- Title: Algebraic Structures: Things I wish someone had explained about functional programming
- Reference: https://jrsinclair.com/articles/2019/algebraic-structures-what-i-wish-someone-had-explained-about-functional-programming
- Category: #article

## Page Notes
## Highlights
- Well, let me ask you a question. Have you ever been around more experienced functional programmers? Ever heard them throwing around a bunch of inscrutable jargon? Words like ‘monoid,’ ‘applicative,’ 'semiring,’ ‘lattice,’ ‘functor,’ or the dreaded ‘monad’? Ever wondered what all that was about? The collective term for these concepts is algebraic structures. — [Updated on 2023-06-30 23:46:41](https://hyp.is/TskYZhddEe6YMYsexSlzTQ/jrsinclair.com/articles/2019/algebraic-structures-what-i-wish-someone-had-explained-about-functional-programming) — Group: #Code
    - Annotation: 在函数式编程领域，有一些术语源自于抽象代数和范畴论，这些概念对于描述数据和操作的组合和交互具有非常强的表现力。这些术语包括：

1. Monoid（幺半群）: 在函数式编程中，Monoid 是一种具有二元运算（一个操作两个参数）和单位元的代数结构。二元运算是满足结合律的，单位元则是这种运算的恒等元素。在 JavaScript 中，可以将数组的 `concat` 方法或整数的加法视为 Monoid。例如，对于加法运算，0 是单位元，因为任何数与 0 相加都等于自身；同时，加法满足结合律，即 `(a + b) + c` 等于 `a + (b + c)`。

2. Applicative（应用函子）: Applicative 是一种函子。函子是一种可以将一个容器内的值通过某种运算映射到另一个容器的结构。Applicative 引入了一个将函子应用于另一个函子的机制，它用于那些不能直接应用普通函数的上下文。

3. Semiring（半环）: 在代数中，Semiring 是一种包含两种运算（通常称为加法和乘法）的结构，这两种运算满足一系列特性，包括结合律、交换律和分配律。在编程中，布尔值就是一个 Semiring 的例子，其中 "加法" 对应于逻辑或，"乘法" 对应于逻辑与。

4. Lattice（格）: Lattice 在编程中可以用来表示数据的部分排序或者多值逻辑系统。它是一个拥有两个特殊二元运算（通常称为 meet 和 join）的代数结构，满足一些特定的规则。

5. Functor（函子）: 在函数式编程中，函子是一种可以对其进行映射操作的结构。在 JavaScript 中，Array 就是一种常见的函子，我们可以使用 `map` 函数对其进行映射操作。

6. Monad（单子）: 在函数式编程中，Monad 是一种可以对其进行链式操作的数据类型。它有两个基本的运算：`return`（也叫 `unit` 或 `of`）和 `bind`（也叫 `>>=` 或 `flatMap`）。`return` 可以将一个值包装到一个 Monad 中，`bind` 可以将一个返回 Monad 的函数应用到一个 Monad。在 JavaScript 的 Promise 就是 Monad 的一个例子：你可以用 `Promise.resolve()`（对应 `return`）将一个值包装为 Promise，然后用 `.then()`（对应 `bind`）将一个返回 Promise 的函数应用到一个 Promise。



