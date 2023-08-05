---
title: week1-Java base
date: 2023-07-11 10:03
article: false
tags: 
---

## Learning philo

[Learning PhiloSophie ▶️ ](https://youtu.be/SixO3uPNAdk?t=1226)

## Pros and Cons Using Typing

The Good:  

- Catches certain types of errors, making it easier for the programmer to debug their code.  
- Type errors can (almost) never occur on end user's computer.  
- Makes it easier to read and reason about code.  
- Code can run more efficiently, e.g., no need to do expensive runtime type checks.

The Bad:  

- Code is more verbose.  
- Code is less general, e.g., there had to be two different `larger` functions earlier.

### 为什么要转成 XX.class

[为什么要编译▶️ ](https://youtu.be/Y2vC_SW00TE?list=PL8FaHk7qbOD5Q4GloF2DHaancV6BOJzL0&t=273)

- class file has been type checked. Distributed code is safer.
- .class files are ‘simpler’ for machine to execute. Distributed code is faster.
- Minor benefit: Protects your intellectual property. No need to give out source.

## static vs non-static

- you'd better access **static things** by class name and access **non-static things** by specific instance.  
•A variable or method defined in a class is also called a member of that class.  
•Static members are accessed using class name, e.g. Dog.binomen.  
•Non-static members cannot be invoked using class name: ~~Dog.makepaise()~

Static methods must access instance variables via a specific instance, e.g. dl.

<img src="http://oss.naglfar28.com/naglfar28/202307111125846.png"/>

### Why java Classes and Static method

Some obvious questions arise:  
●Why does Java force us to use classes?  
●Why have static methods at all? 

The reason: To take choices away from the programmer. 

- Fewer choices means fewer ways to do things. 
	- Example: Declaring a method static means you can’t use any instance variables in that method.  
- Fewer ways to do things often means less complexity.

## Help method

什么是 Help Method[▶️ ](https://youtu.be/23gXoMFRY9Q?list=PL8FaHk7qbOD5Q4GloF2DHaancV6BOJzL0&t=32)
