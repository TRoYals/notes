---
title: 287_leetcode
date: 2023-11-09 12:34
article: false
tags: 
cards-deck: 04 Coding & Tech::04 Coding Ability::00 Leetcode::leetcode
---

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.  
There is only **one repeated number** in `nums`, return _this repeated number_.  
You must solve the problem **without** modifying the array `nums` and uses only constant extra space.  
#card
```
impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let mut slow = nums[0] as usize;
        let mut fast = nums[0] as usize;
        loop {
            slow = nums[slow] as usize;
            fast = nums[nums[fast] as usize] as usize;
            if slow == fast {
                break;
            }
        }
        fast = nums[0] as usize;
        while slow != fast {
            slow = nums[slow] as usize;
            fast = nums[fast] as usize;
        }
        slow as i32
    }
}
```
[[../算法/Floyd循环算法|Floyd循环算法]]  
注意的地方:
1. 使用 数组模拟指针  
^1699504645396
