---
title: Dynamic Games of Complete Information
date: 2023-05-03 12:53
article: false
star: false
---

## Dynamic Games with Complete and Perfect Information
The key features are: 

(i) the moves occur in sequence; 

(ii) all previous moves are observed before the next move is chosen, (perfect information); 

(iii) the players’ payoffs from each combination of moves are common knowledge, (complete information).

### backwards-induction outcome
通过从最终结果开始向后推导，确定每个参与者在每个阶段应该采取的最优策略。
![](http://oss.naglfar28.com/naglfar28/202305031301522.png)
LR玩家先选，选择R，则L‘R’玩家必须选L‘。 这就是先发制人的优势。

### A three-move game
![image.png](http://oss.naglfar28.com/naglfar28/202305031305144.png)
![image.png](http://oss.naglfar28.com/naglfar28/202305031305085.png)

怎么推？ 倒推！

1. 对于玩家1 在第三阶段，选择L'''的收益最高（**3**，0），所以在第三阶段一定会选L'''
2. 对于玩家2在第二阶段，选择L''的收益是（1，**1**），但是选择R''会步入推导1，此时收益是0，所以一定会选择L'。
3. 已经知道玩家2在第二阶段会选择L',此时自己的收益是1，所以直接在第一阶段选择L 即可。　

The backwards-induction outcome: Player 1 plays I at the first stage, and the game ends.

### stackelberg Model of Duopoly
![image.png](http://oss.naglfar28.com/naglfar28/202305031310427.png)
怎么做？

1. 假设已经知道，q1，求出q2的表达式。
2. 把算出来的q2带入到步骤一，求q1。　

## Two-Stage Games of Complete But Imperfect Information

### subgame-perfect Outcome
![image.png](http://oss.naglfar28.com/naglfar28/202305031329875.png)
![image.png](http://oss.naglfar28.com/naglfar28/202305031329572.png)

### Tariff Game
![](http://oss.naglfar28.com/naglfar28/202305031335922.png)

<img src="http://oss.naglfar28.com/naglfar28/202305031335848.png"/>
<img src="http://oss.naglfar28.com/naglfar28/202305031336674.png"/>
<img src="http://oss.naglfar28.com/naglfar28/202305031336111.png"/>
<img src="http://oss.naglfar28.com/naglfar28/202305031337393.png"/>

## Extensive-form representation of Games

The extensive-form representation of a game specifies 

(1) the players in the game; 

(2a) when each player has the move,

(2b) what each player can do at each of his or her opportunities to move, 

(2c) what each player knows at each of his or her opportunities to move; 

(3) the payoffs received by each player for each combination of moves that could be chosen by the players.

![image.png](http://oss.naglfar28.com/naglfar28/202305031341151.png)

A dynamic game of complete and perfeet information is a game in which the players move in sequence, all previous moves are observed before the next move is chosen, and payoffs are common knowledge. Such games can be easily represented by a game tree.

When information is not perfect, some previous moves are not observed by the player with the current move. To present this kind of ignorance of previous move and to describe what each player knows at each of his/her move, we introduce the notion of a player's information set.

```ad-tip Information Set
 An information set for a player is a collection of decision nodes satisfying:
1. The player needs to move at every node in the information set.
2. When the play of the game reached a node in the information set, the player with the move does not kenow which node in the set has (or has not) been reached.　
　

```

- Point 2 implies that the player must have the same set of feasible actions at each decision node in an information set.
- A game is said to have imperfect information if some of its information sets are nonsingletons.
- In an extensive-form game, a collection of decision nodes, which constitutes an information set, is connected by a dotted line.　

1. static game of complete information can be represented by dynamic games of complete but imperfect information.　


### Subgame-perfect Nash eq
考虑这个例子
![image.png](http://oss.naglfar28.com/naglfar28/202305031357025.png)

为什么会出现明显错误的Nq，可以想像成一个出于害怕的防守?




