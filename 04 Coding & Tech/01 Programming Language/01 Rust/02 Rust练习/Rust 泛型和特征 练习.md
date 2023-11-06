---
title: Rust 泛型和特征 练习
date: 2023-11-01 13:43
article: false
tags: 
---

```rust
struct Point<T, U> {
    x: T,
    y: U,
}
impl<T, U> Point<T, U> {
    // 实现 mixup，不要修改其它代码！
    fn mixup
}
fn main() {
    let p1 = Point { x: 5, y: 10 };
    let p2 = Point { x: "Hello", y: '中'};
    let p3 = p1.mixup(p2);
    assert_eq!(p3.x, 5);
    assert_eq!(p3.y, '中');
}
```
#card 
```rust
struct Point<T, U> {
    x: T,
    y: U,
}
impl<T:Copy, U> Point<T, U> {
    // 实现 mixup，不要修改其它代码！
    fn mixup<V,W>(&self,other:Point<V,W>)->Point<T,W>{
		Point{
			x: self.x,
			y:other.y
		}
	}
}
fn main() {
    let p1 = Point { x: 5, y: 10 };
    let p2 = Point { x: "Hello", y: '中'};
    let p3 = p1.mixup(p2);
    assert_eq!(p3.x, 5);
    assert_eq!(p3.y, '中');
}


