---
title: CS61B-Proj0
date: 2023-07-14 10:30
article: false
tags: 
---

## 背景
### resources

[Project 0: 2048 | CS 61B Spring 2021](https://sp21.datastructur.es/materials/proj/proj0/proj0)!

## Assignment Philosophy and Program Design
### MVC pattern

The MVC pattern divides our problem into three parts:

- The **model** represents the subject matter being represented and acted upon – in this case incorporating the state of a board game and the rules by which it may be modified. Our model resides in the `Model`, `Side`, `Board`, and `Tile` classes. The instance variables of `Model` fully determine what the state of the game is. Note: You’ll only be modifying the `Model` class.
- A **view** of the model, which displays the game state to the user. Our view resides in the `GUI` and `BoardWidget` classes.
- A **controller** for the game, which translates user actions into operations on the model. Our controller resides mainly in the `Game` class, although it also uses the GUI class to read keystrokes.

The second pattern utilized is the “Observer pattern”. Basically this means that the **model** doesn’t actually report changes to the **view**. Instead, the **view** _registers_ itself as an _observer_ of the `Model` object. This is a somewhat advanced topic so we will provide no additional information here.

