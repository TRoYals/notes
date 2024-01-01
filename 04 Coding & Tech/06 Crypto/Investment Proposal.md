# Investment Proposal

## 背景

### 交易平台

在本篇论文中，我们将制定一个用于加密货币交易的算法。加密货币交易是一个快速发展的领域，以其高波动性和 24 小时不间断的交易环境而闻名。这一特性提供了独特的交易机会，但也带来了相应的挑战。鉴于此，选择一个合适的交易平台对于我们整个投资提案的成功至关重要。理想的交易平台应具备以下特点：

高频交易能力：在加密货币市场，价格可能在很短的时间内发生大幅波动。因此，能够快速执行交易的平台对于抓住这些短暂机会至关重要。  
实际操作能力：我们需要一个能够实际部署和执行我们算法的平台，而不仅仅是理论上的模拟环境。  
多货币对支持：为了验证我们算法的通用性和适应性，平台需要支持多种加密货币对的交易。  
可控性：在加密货币交易中，控制风险至关重要。我们需要一个允许我们精确控制交易细节的平台，尽可能减少依赖于第三方服务的风险。

基于以上要求, 我们选择了 Freqtrade 这个开源交易平台, 这是一个基于 Python 开发的高频交易机器人, 项目在 github 上有 23.6kstars. 这个平台满足我们对交易平台的需求, 同时该平台也可以进行简单的回测来测试我们的交易算法的利润率.

## 数据源

考虑到数据的可靠性和广泛性，我们选择了 Binance 作为我们的主要数据源。Binance 是全球最大的加密货币交易所之一，提供广泛的货币对和丰富的市场数据.考虑到我们的算法是短期交易，我们选择了 5 分钟的 K 线数据作为我们的主要数据源。通过选择 "BTC/USDT",  
"BCH/USDT",  
"ETH/USDT",  
"LINK/USDT",  
"LTC/USDT",  
"SOL/USDT",  
"BNB/USDT",  
"XRP/USDT",  
"ADA/USDT",  
"DOT/USDT",  
"ETC/USDT",  
"ALGO/USDT",  
 12 个交易对作为可供交易的对象.

## 算法设计

### 算法概述

我们的投资算法是一种自动化交易策略，主要应用于金融市场的技术分析。它融合了多种技术指标，如指数移动平均线（EMA）、霍尔移动平均线（HMA）、相对强弱指数（RSI）和艾略特波动振荡器（EWO），以形成综合的交易决策框架。此策略的核心目的是通过识别市场趋势和动量变化，来优化买卖点的选择，从而增加交易成功率和盈利潜力。

### 算法指标

#### EMA 指数移动平均线

**指数移动平均线（EMA）**是技术分析中用于识别市场趋势的工具。与简单移动平均线不同，EMA 更加重视近期价格数据，使其能够更快响应市场变化。投资者通常利用 EMA 来判断趋势方向，其中短期 EMA 超过长期 EMA 可能表明上升趋势，反之则可能表示下跌趋势。

#### HMA 霍尔移动平均线

霍尔移动平均线（HMA），由阿兰·霍尔（Alan Hull）于 2005 年提出，是一种极为平滑且几乎无滞后的移动平均线。HMA 的设计旨在克服传统移动平均线的主要弱点：滞后。通过计算加权移动平均线的平均数，并应用平方根作为周期，HMA 提供了比标准移动平均线更快的反应速度。这使得 HMA 成为捕捉趋势早期变化的理想工具，尤其适用于快速变化的市场环境。因其平滑的特性，HMA 也常用于确定市场趋势和潜在的转变点。

#### RSI 相对强弱指

相对强弱指数（RSI）是由 J. Welles Wilder Jr. 在 1978 年开发的一种动量振荡器，用于衡量资产价格变动的速度和幅度。RSI 值范围从 0 到 100，通常用于识别市场的超买或超卖状态。标准的 RSI 周期为 14 天，但可以根据交易策略调整。

当 RSI 值超过 70 时，市场可能处于超买状态，意味着价格可能会下跌；当 RSI 值低于 30 时，市场可能处于超卖状态，意味着价格可能会上涨。RSI 还可以用于识别潜在的市场反转点，通过观察 RSI 与价格走势的背离。例如，如果价格创新高而 RSI 未能创新高，这可能预示着即将发生趋势反转。RSI 是交易者和投资者广泛使用的工具，适用于各种市场和时间框架。

#### EWO

艾略特波动振荡器（EWO）是根据艾略特波理论（Elliott Wave Theory）设计的一个技术分析工具。EWO 的主要目的是帮助交易者识别市场动力的变化和趋势的可能转折点。这个指标通过计算两个不同周期的指数移动平均线（EMA）之间的差异来实现。

具体来说，EWO 通常通过从较短周期的 EMA 中减去较长周期的 EMA 来计算。例如，常见的做法是使用 5 天和 35 天的 EMA。当 EWO 值为正，表明短期动量超过长期动量，可能表示市场趋势向上；当 EWO 值为负，表明长期动量占优，可能表示市场趋势向下。

### 算法流程

## 算法实现

本文中的算法实现基于 Python 语言，主要使用了以下三方库：  
talib.ta-lib 是一个用于技术分析的 Python 库，提供了 150 多种技术指标的实现。

### 各指标计算

该算法具体涉及到以下几个参数:

RSI: 会选择 14 个周期作为 RSI 的计算周期。同时会选用 4 个周期作为快速 RSI 的计算周期，以及 20 个周期作为慢速 RSI 的计算周期。

HMA: 会选择 50 个周期作为 HMA 的窗口周期。

Offset: 选择 1.008 作为 high Offset 的值,选择 0.987 作为 low Offset 的值。  
各参数的计算公式如下:

```python
    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        # Calculate all ma_buy values
        for val in self.base_nb_candles_buy.range:
            dataframe[f'ma_buy_{val}'] = ta.EMA(dataframe, timeperiod=val)

        # Calculate all ma_sell values
        for val in self.base_nb_candles_sell.range:
            dataframe[f'ma_sell_{val}'] = ta.EMA(dataframe, timeperiod=val)

        dataframe['hma_50'] = qtpylib.hull_moving_average(dataframe['close'], window=50)


        dataframe['sma_9'] = ta.SMA(dataframe, timeperiod=9)
        # Elliot
        dataframe['EWO'] = EWO(dataframe, self.fast_ewo, self.slow_ewo)

        # RSI
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        dataframe['rsi_fast'] = ta.RSI(dataframe, timeperiod=4)
        dataframe['rsi_slow'] = ta.RSI(dataframe, timeperiod=20)

```

### entry point

该算法拥有两个买入策略, 分别如下:

```python
        conditions.append(
            (

                (dataframe['rsi_fast'] <35)&
                (dataframe['close'] < (dataframe[f'ma_buy_{self.base_nb_candles_buy.value}'] * self.low_offset.value)) &
                (dataframe['EWO'] > self.ewo_high.value) &
                (dataframe['rsi'] < self.rsi_buy.value) &
                (dataframe['volume'] > 0)&
                (dataframe['close'] < (dataframe[f'ma_sell_{self.base_nb_candles_sell.value}'] * self.high_offset.value))


            )
        )

        conditions.append(
            (


                (dataframe['rsi_fast'] < 35)&
                (dataframe['close'] < (dataframe[f'ma_buy_{self.base_nb_candles_buy.value}'] * self.low_offset.value)) &
                (dataframe['EWO'] < self.ewo_low.value) &
                (dataframe['volume'] > 0)&
                (dataframe['close'] < (dataframe[f'ma_sell_{self.base_nb_candles_sell.value}'] * self.high_offset.value))

            )
        )
```

这个交易策略包括两种不同的买入条件，旨在识别市场的低点买入机会。这些条件结合了多个技术指标来确定最佳买入时机。

第一种买入条件：这个条件考虑了相对强弱指数（RSI）的快速变化，EMA（指数移动平均线）的特定价位，以及 EWO（Elliot 波动振荡器）的高值。这种组合指向市场处于超卖状态但开始出现上升趋势的可能性。当 RSI 快速下降到 35 以下，EWO 高于设定的高值，且股价低于基于 EMA 调整的价位时，触发买入信号。

第二种买入条件：这个条件依然使用 RSI 和 EMA 的组合，但在 EWO 的使用上有所不同，寻找 EWO 的低值。这表明市场可能在短期内被高度低估。当 RSI 快速下降，EWO 低于设定的低值，且股价低于基于 EMA 调整的价位时，同样触发买入信号。

这两种条件的共同点是，它们都寻找市场的超卖状态，并利用 EMA 和 EWO 的不同组合来确定买入时机，尝试在市场反弹之前抓住机会。

### exit point

同样的,我们为该算法设计了两个卖出条件

```python

        conditions.append(
            (   (dataframe['close']>dataframe['hma_50'])&
                (dataframe['close'] > (dataframe[f'ma_sell_{self.base_nb_candles_sell.value}'] * self.high_offset_2.value)) &
                (dataframe['rsi']>50)&
                (dataframe['volume'] > 0)&
                (dataframe['rsi_fast']>dataframe['rsi_slow'])

            )
            |
            (
                (dataframe['close']<dataframe['hma_50'])&
                (dataframe['close'] > (dataframe[f'ma_sell_{self.base_nb_candles_sell.value}'] * self.high_offset.value)) &
                (dataframe['volume'] > 0)&
                (dataframe['rsi_fast']>dataframe['rsi_slow'])
            )

        )
```

此交易策略也设计了两种卖出条件，用以确定何时退出市场以锁定利润或减少损失。

第一种卖出条件：此条件针对的是市场的上升趋势。当股价高于 HMA（Hull 移动平均线）和基于 EMA 调整的特定价位，且 RSI 指示市场进入超买状态时，触发卖出信号。这表明股价可能已达到短期高点，是时候获利了结。

第二种卖出条件：此条件则关注市场的下跌趋势。即使股价处于 HMA 以下，只要高于基于 EMA 调整的另一特定价位，并且 RSI 快速上升超过慢速 RSI，也会触发卖出信号。这可能表明尽管市场整体趋势向下，但股价短期内有上涨，提供了获利了结的机会。

总体来说，这些卖出条件结合了移动平均线和 RSI 指标，以识别市场潜在的高点，从而在合适的时机退出交易。

### risk control

在进行自动交易时，风险控制是至关重要的部分。Freqtrade 提供了一个强大的内置风险管理系统，使交易者能够实施多种风险控制措施。这些措施旨在优化交易策略，同时减少潜在的财务损失。以下是这些措施的详细说明及其对交易策略的影响：

冷却期（Cooldown Period）:  
冷却期是一种在遭遇连续损失或大幅下跌后自动启动的机制。它通过暂停交易活动一段时间（如 5 个蜡烛图时间），帮助避免在不利市场情绪或过度波动的环境中继续交易。这有助于防止由恐慌驱动的决策，保护投资者免受连续损失的影响。  
移动止损（Trailing Stop Loss）:  
移动止损是一种动态的风险管理工具，允许设置一个随市场价格变动而调整的止损点。这意味着当交易处于盈利状态时，止损点会自动上调，以保护已获得的利润。此策略在波动的市场中特别有效，因为它既保护了盈利，又为价格回调提供了空间。  
交易对暂停（Pair Stop Loss）:  
当特定的交易对在一定时间内的表现低于预期（如在 6 个蜡烛图时间内利润低于 2%）时，系统会暂停交易该对。这有助于避免在某些特定的不利市场条件下持续亏损。通过及时停止交易低利润对，策略能够将资源重新分配到更有利可图的交易对。  
最大开仓数限制（Max Open Trades）:  
此措施限制同一交易对的最大开仓数，有助于分散风险并避免过度集中于单一市场。通过限制同一交易对的开仓数量，可以防止因某一市场突发事件而产生过大损失。  
投资回报率（ROI）:  
ROI 设置根据交易持续的时间来确定不同的卖出点。例如，策略可以设置在交易开始后的第一个时间单位内以 99% 的回报率卖出，以快速获利或减损。随着持仓时间的增加，这个目标可以调整，以适应市场的长期趋势。这个策略帮助交易者在不同的市场条件下实现最佳的利润。  
总而言之，通过综合使用这些风险控制措施，自动交易策略能够更加灵活地应对市场的不确定性和波动性。这些措施的组合不仅有助于保护投资者的资本免受重大损失，而且有助于优化交易表现，确保在各种市场条件下都能实现稳健的回报。

### backtesting

在评估我们的投资提案中，对所选择的交易策略进行了细致的回测分析，以确保我们的投资决策建立在经过验证的策略基础上。以下是 2023 年 6 月 1 日至 12 月 1 日间进行的回测具体内容。

============================================================ BACKTESTING REPORT ===========================================================  
| Pair | Entries | Avg Profit % | Cum Profit % | Tot Profit USDT | Tot Profit % | Avg Duration | Win Draw Loss Win% |  
|-----------+-----------+----------------+----------------+-------------------+----------------+----------------+-------------------------|  
| LTC/USDT | 8 | 1.95 | 15.60 | 3386.272 | 3.39 | 1:38:00 | 7 0 1 87.5 |  
| BCH/USDT | 35 | 0.37 | 12.96 | 2543.963 | 2.54 | 2:09:00 | 19 0 16 54.3 |  
| SOL/USDT | 33 | 0.34 | 11.13 | 2208.054 | 2.21 | 2:09:00 | 21 0 12 63.6 |  
| ADA/USDT | 8 | 1.06 | 8.50 | 1762.804 | 1.76 | 1:51:00 | 6 0 2 75.0 |  
| ALGO/USDT | 6 | 1.16 | 6.99 | 1498.001 | 1.50 | 1:57:00 | 5 0 1 83.3 |  
| LINK/USDT | 27 | 0.06 | 1.64 | 399.767 | 0.40 | 2:06:00 | 14 0 13 51.9 |  
| ETH/USDT | 2 | 0.38 | 0.76 | 163.654 | 0.16 | 3:20:00 | 1 0 1 50.0 |  
| ETC/USDT | 11 | 0.08 | 0.93 | 131.825 | 0.13 | 2:26:00 | 7 0 4 63.6 |  
| BTC/USDT | 2 | 0.30 | 0.60 | 128.655 | 0.13 | 2:48:00 | 1 0 1 50.0 |  
| DOT/USDT | 2 | 0.10 | 0.20 | 44.875 | 0.04 | 3:20:00 | 1 0 1 50.0 |  
| BNB/USDT | 0 | 0.00 | 0.00 | 0.000 | 0.00 | 0:00 | 0 0 0 0 |  
| XRP/USDT | 8 | -0.22 | -1.73 | -398.966 | -0.40 | 2:30:00 | 4 0 4 50.0 |  
| TOTAL | 142 | 0.41 | 57.58 | 11868.904 | 11.87 | 2:10:00 | 86 0 56 60.6 |

================== SUMMARY METRICS ==================  
| Metric | Value |  
|-----------------------------+---------------------|  
| Backtesting from | 2023-06-01 00:00:00 |  
| Backtesting to | 2023-12-01 00:00:00 |  
| Max open trades | 5 |  
| | |  
| Total/Daily Avg Trades | 142 / 0.78 |  
| Starting balance | 100000 USDT |  
| Final balance | 111868.904 USDT |  
| Absolute profit | 11868.904 USDT |  
| Total profit % | 11.87% |  
| CAGR % | 25.07% |  
| Sortino | 3.49 |  
| Sharpe | 2.32 |  
| Calmar | 22.82 |  
| Profit factor | 1.46 |  
| Expectancy (Ratio) | 83.58 (0.18) |  
| Trades per day | 0.78 |  
| Avg. daily profit % | 0.06% |  
| Avg. stake amount | 21722.042 USDT |  
| Total trade volume | 3084530.034 USDT |  
| | |  
| Best Pair | LTC/USDT 15.60% |  
| Worst Pair | XRP/USDT -1.73% |  
| Best trade | LTC/USDT 7.20% |  
| Worst trade | LINK/USDT -6.69% |  
| Best day | 3593.433 USDT |  
| Worst day | -2260.534 USDT |  
| Days win/draw/lose | 19 / 123 / 18 |  
| Avg. Duration Winners | 1:25:00 |  
| Avg. Duration Loser | 3:20:00 |  
| Max Consecutive Wins / Loss | 11 / 5 |  
| Rejected Entry signals | 2 |  
| Entry/Exit Timeouts | 0 / 0 |  
| | |  
| Min balance | 100336.223 USDT |  
| Max balance | 114921.77 USDT |  
| Max % of account underwater | 5.43% |  
| Absolute Drawdown (Account) | 5.43% |  
| Absolute Drawdown | 6241.141 USDT |  
| Drawdown high | 14921.77 USDT |  
| Drawdown low | 8680.628 USDT |  
| Drawdown Start | 2023-10-23 05:15:00 |  
| Drawdown End | 2023-11-09 18:40:00 |  
| Market change | 33.44% |

盈利性与效率:  
策略展现了显著的盈利性，总利润率达到 11.87%，即 11868.904 USDT 的绝对盈利。每日平均交易次数为 0.78 次，显示出适度的交易活跃度。特别是在 LTC/USDT 交易对上，策略表现最为突出，实现了 15.60% 的利润率。

风险控制与管理:  
从风险管理的角度来看，Sortino 比率为 3.49，Sharpe 比率为 2.32，表明策略在考虑风险的情况下提供了良好的回报。最大账户回撤控制在 5.43% 内，证明策略具有有效的损失控制机制。

胜率与持续时间:  
策略整体胜率为 60.6%，其中在 LTC/USDT 交易对上的胜率高达 87.5%。平均持仓时间为 2 小时 10 分钟，这表明策略主要聚焦于短至中期的交易。

市场适应性:  
在考虑市场整体变化（33.44%）的情况下，策略能够适应市场波动并实现稳定的盈利。这一点在各交易对的表现中得到了证实，尽管存在如 XRP/USDT 这样表现不佳的交易对。

