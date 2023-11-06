---
title: AMM
date: 2023-10-21 20:11
article: false
tags: 
---
**Section 1: AMM, trading and arbitrage**

Alice and Bob are trading token "A" on Uniswap, which is a constant product AMM. We have an A-USDC liquidity pool on Uniswap (i.e. a pool with two assets). The pool currently has 10,000 A token and 20,000 USDC. In the following assume that there is no swap fee nor any gas fees for the transactions.

1. What is the current price of token A?

Answer: 2 USDC

Transaction 1: Alice buys 2,000 token A from the pool.

2. How much USDC should Alice spend to buy token A?

Answer: 5000 USDC

```
10000*20000=8000*x
x = 25000
```

3. What is the market price of token A after Transaction 1? (in USDC)

Answer: 3.125 USDC 

Transaction 2: After Transaction 1 executed successfully on Ethereum, Bob buys 3,000 token A from the pool.

4. How much USDC should Bob spend to buy token A?

Answer: 15000 USDC

```
10000*20000 = 5000*x
x = 40000
40000-25000 = 15000
```
5. What is the market price of token A after Transaction 2 completed?

Answer: 8 USDC/token A

Transaction 3: After Transaction 2 executed successfully on Ethereum, Alice sells all her 2,000 token A from the pool.

6. What is the total profit of Alice made from Transaction 1 and Transaction 3? (in USDC)

Answer: 6428.57 USDC

```
5000*40000 = 7000*x
x = 28571.43 USDC
40000- 28571.43 = 11428.57
11428.57-5000=6428.57 USDC
```

7. What is the market price of token A after Transaction 3 completed?

Answer: 4.081 USDC

**Section 2:  Impermanent Loss**

Suppose we had a Uniswap liquidity pool in January 2021, the pool had 1,000 ETH and 1,000,000 USDT after Alice joined the pool. Alice owned 2% of the total liquidity with 20 ETH paired with some USDT.

1. How much USDT should be paired with the 20 ETH for Alice to join the pool?

Answer: 20000 USDT

2. What was the market price of ETH when Alice joined the pool? (in USDT)  
	Answer: 1000 USDT

3. In May 2021, Alice removed all her liquidity in the pool when the market price of ETH was 4000 USDT. How much ETH and USDT did she receive after she withdrew her liquidity?  
	Answer: 10ETH 4000USDT

4. What is the impermanent loss of Alice? (in USDT)

Answer: 20000 USDT

5. What is the percentage of impermanent loss (i.e., percentage change in total equity value) for Alice?  
	Answer: 20%

6. Now we consider the general case of impermanent loss. If the price of ETH pumps to N times of the original price. What is the percentage of impermanent loss (i.e., percentage change in total equity value) for the liquidity providers? Please explain how you get the answer as well.  
	Answer:
 
Certainly! Let's derive the impermanent loss for the general case where the price of ETH pumps to \(N\) times its original price. To simplify the calculations, we'll use the formula for the constant product AMM (automated market maker) model that Uniswap and other decentralized exchanges utilize.

### Initial Situation

Let's start with a pool having:
- 1 ETH and 
- \(P\) USDT (where \(P\) is the price of ETH in USDT initially).

Using the constant product formula:  
\[k = \text{ETH balance} \times \text{USDT balance} \]  
Initially, \(k = 1 \times P = P\).

### When ETH Price Increases by Factor N

If the price of ETH outside the pool increases to \(N \times P\), arbitrageurs will trade with the pool until the price inside the pool reflects this new price.

Let's say after arbitrage, the pool has \(ETH_{new}\) ETH left. The USDT balance would then be \(\frac{k}{ETH_{new}} \).

The price inside the pool after arbitrage would be:  
\[\text{Price} = \frac{\frac{k}{ETH_{new}}}{ETH_{new}} \]  
Given that this has to equal the new price \(N \times P\):
\[ \frac{P}{ETH_{new}^2} = N \times P \]

Solving for \(ETH_{new}\):
\[ ETH_{new}^2 = \frac{1}{N} \]
\[ ETH_{new} = \sqrt{\frac{1}{N}} \]

### Calculating Impermanent Loss

Now, let's consider a liquidity provider who initially provided 1 ETH and \(P\) USDT.

Had they just held onto their assets without providing liquidity, after the price increase they would have assets worth:
\[ 1 \times N \times P = N \times P \]

But, from the pool, they would withdraw:
\[ ETH_{new} \times N \times P \]
Which is:
\[ \sqrt{\frac{1}{N}} \times N \times P = \sqrt{N} \times P \]

The impermanent loss is:
\[ IL = N \times P - \sqrt{N} \times P \]

The percentage impermanent loss is:
\[ \text{Percentage IL} = \frac{IL}{N \times P} \times 100\% \]
\[ = \frac{N \times P - \sqrt{N} \times P}{N \times P} \times 100\% \]
\[ = \left(1 - \sqrt{\frac{1}{N}}\right) \times 100\% \]

This formula gives the percentage impermanent loss for a liquidity provider when the price of ETH increases by a factor of \(N\).

**Section 3:  Liquidity mining and DEX's business model**

MQFswap is a DEX using liquidity mining incentives for the launch of its governance token MQF. We consider a simple case of MQFswap with its previous constant product AMM.

1. Bob is a liquidity provider for MQFswap ETH-USDC pool. Suppose the total liquidity for the pool is 1000 ETH and 2,000,000 USDC currently, and Bob owns 2% of the pool. The liquidity mining reward for this pool is 1000 MQF per day. We suppose that the percentage owned by Bob of the liquidity pool will not change. How many MQF can Bob earn per day?  
	Answer:  

2. If the current price of MQF is 8 USDC. What is the current APY (i.e., Annual Percentage Yield) through farming MQF? (We don’t consider the compound interest in the APY calculation)  
	Answer:  

MQFswap charges 0.3% trading fee in each swap. 0.25% of the trading fee will be fairly distributed to all the liquidity providers of each pool (We consider the 0.25% trading fee to be the profit earned by the liquidity providers) and 0.05% of the trading fee will be distributed to the MQF token stakers (We consider the 0.05% trading fee to be the profit earned by the protocol, and fairly distributed to its community governors).  

3. Suppose the total trading volume is 1,000,000 USDC for the ETH-USDC pair today. What is the trading fee earned by Bob? (in USDC)  
	Answer:  

4. What is the current APR from the trading fee?  
	Answer:

Suppose the total circulation of MQF token is 200,000,000. Trading volume today is 200,000,000 USDC.  

5. What’s the total revenue for MQF stakers for today? (in USDC)  
	Answer:  

6. Suppose 25% of the total circulated MQF token is staked in the protocol. Then what is the current APR for MQF stakers?  
	Answer:

7. Calculate the P/E ratio of MQFswap. In general, we can calculate the P/E ratio of a DEX by using the total circulated market cap divided by the annual profits earned by the protocol. Now let’s try to calculate the P/E ratio of MQFswap from the above data (Suppose the price of MQF is 8 USD). To compute the profits, we only consider the profits earned by the protocol (0.05% of the total trading volume in MQFswap).  
Answer: