---
title: Floyd循环算法
date: 2023-11-09 11:02
article: false
tags: 
leetcode: 287
cards-deck: 04 Coding & Tech::04 Coding Ability::00 Leetcode::算法
---

## 写在前面 
#card  
leetcode 287  
^1699502980029

##

这是一个很好的问题，Floyd 的循环查找算法中确实会出现这样的情况。这里有一个数学证明，可以解释为什么以相同的速度从不同的起点出发的两个指针会在循环的起始点相遇。

让我们定义几个变量来帮助理解这个过程：

- 设链表的非循环部分的长度为 `F`（从链表头到循环开始的部分）。
- 设循环部分的长度为 `C`。
- 当两个指针首次相遇时，假设慢指针已经在循环里走了 `a` 步，因此它距离循环的起始点有 `C - a` 步。
- 此时，快指针已经在循环里走了 `a + nC` 步（因为它可能已经在循环里跑了多圈），其中 `n` 是快指针在循环中跑了多少圈的整数。

当快慢指针首次在循环中相遇时，由于快指针的速度是慢指针的两倍，我们可以得到以下等式：

\[2(F + a) = F + a + nC \]

这个等式简化后得到：

\[F + a = nC \]

这意味着从链表头到循环开始的长度 `F` 加上慢指针在循环中走的长度 `a` 等于循环长度 `C` 的整数倍。

如果此时我们把一个指针放回链表的起始点，然后两个指针都以速度 1 前进，它们最终会在循环的起始点相遇，因为：

- 慢指针需要走 `C - a` 步到达循环的起始点。
- 同时，从链表头出发的指针会走 `F` 步到达循环的起始点。

由于 `F` 正好是 `C` 的整数倍减去 `a`（即 `F = nC - a`），这就意味着当两个指针再次相遇时，它们都恰好到达了循环的起始点。

这个数学性质是算法能够工作的关键所在，它保证了不管循环有多长，两个指针最终都会在循环的起始点相遇。

当然，让我们用一个简单的例子来说明 Floyd 的循环查找算法是如何工作的。

假设我们有一个数组 `nums = [1, 3, 4, 2, 2]`，这个数组中的每个数值可以代表指向下一个索引的指针，形成一个隐式的链表。根据数组索引和值的关系，我们可以得到以下链表表示：

```
index: 0 1 2 3 4
value: 1 3 4 2 2
```

这个隐式链表就像这样：

```
0 -> 1 -> 3 -> 2 -> 4
         ^         |
         |_________|
```

在这个链表中，索引 `3` 指向索引 `2`，索引 `2` 指向索引 `4`，而索引 `4` 指向索引 `2`，形成了一个循环。

现在，让我们应用 Floyd 的算法：

1. **初始化两个指针**：一个快指针 `fast` 和一个慢指针 `slow`。它们都开始在索引 `0`。
2. **移动指针**：
   - 慢指针每次移动一步：`slow = nums[slow]`。
   - 快指针每次移动两步：`fast = nums[nums[fast]]`。

如果我们按照上面的规则移动指针，情况将会如下：

- 初始状态：`slow` 指向 `1`，`fast` 也指向 `1`。
- 第一步：`slow` 移动到 `3`，`fast` 移动到 `2`。
- 第二步：`slow` 移动到 `2`，`fast` 移动到 `2`。

这时，快慢指针在索引 `2` 处相遇。这告诉我们链表中存在一个循环。

3. **找到循环的起始点**：
   - 将快指针或慢指针重置回起点 `0`。
   - 然后两个指针都以每次一步的速度移动。

我们继续移动两个指针：

- `slow` 指向 `2`，`fast` 重置后指向 `1`。
- `slow` 移动到 `4`，`fast` 移动到 `3`。
- `slow` 移动到 `2`（因为 `nums[4]` 是 `2`），`fast` 移动到 `2`（因为 `nums[3]` 是 `2`）。

这时，快慢指针再次相遇，而且它们相遇在值为 `2` 的节点上，这就是数组中重复的数。

通过这个例子，我们可以看到，即使快慢指针起始于不同的位置，它们最终还是会在循环的起始位置相遇。这个属性是由链表中的循环结构决定的，并且被 Floyd 算法利用来检测循环并找到循环开始的地方。

## 相关资料

Rust 中使用枚举实现链表  
#card  
[rust-by-practice/solutions/compound-types/enum.md at master · sunface/rust-by-practice](https://github.com/sunface/rust-by-practice/blob/master/solutions/compound-types/enum.md)  
[枚举 - Rust By Practice( Rust 练习实践 )](https://zh.practice.rs/compound-types/enum.html)  
^1699502980034  

如果你想练习使用 Floyd 的循环检测算法，你可以尝试解决以下几类问题：

1. **环形链表**：给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回 `null`。
2. **重复数字**：如同你之前的问题，给定一个长度为 `n+1` 的数组，所有数字都在 `1` 到 `n` 之间（包括 `1` 和 `n`），其中只有一个数字是重复的。找出这个重复的数字，不要修改原数组，只使用常数额外空间。
3. **循环序列**：给你一个序列，其中包含一个循环。序列的下一个值由一个已知的函数 `f` 计算得出。找到循环的开始位置。
4. **随机数生成器周期**：使用一个随机数生成器，它按照固定的算法产生一个无限的随机数序列。尽管序列是无限的，但随机数生成器的内部状态是有限的，所以序列最终会开始重复。使用 Floyd 的循环检测算法找到重复序列的开始。

这些问题都可以使用 Floyd 的循环检测算法来解决。为了编写解决方案，你需要理解如何在各自的问题上应用算法，如何确定“快”和“慢”指针的移动规则，以及如何确定循环开始的点。

例如，对于环形链表问题，以下是一个 Rust 中的解决方案：

```rust
// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn detect_cycle(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut slow = head.as_ref();
        let mut fast = head.as_ref();

        while let (Some(s_node), Some(f_node)) = (slow, fast.and_then(|n| n.next.as_ref())) {
            slow = s_node.next.as_ref();
            fast = f_node.next.as_ref();
            if slow == fast {
                // Found the cycle, now find the entry point
                let mut slow = head.as_ref();
                let mut fast = fast; // Keep the fast where they met
                while slow != fast {
                    slow = slow.unwrap().next.as_ref();
                    fast = fast.unwrap().next.as_ref();
                }
                return slow.cloned(); // or fast.cloned();
            }
        }

        None // No cycle found
    }
}
```

在这段代码中，我们首先检测链表中是否存在循环。如果存在循环，我们找到快慢指针相遇的点。然后，我们将一个指针移动回链表的头部，并以相同的速度移动两个指针直到它们再次相遇，这个相遇点就是循环的入口。