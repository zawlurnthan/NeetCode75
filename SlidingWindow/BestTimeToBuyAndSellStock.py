"""
    121. Best Time to Buy and Sell Stock
    Easy

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a
    different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any
    profit, return 0.

    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.


    Constraints:

    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1
    maxP = 0

    # iterate by right pointer
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP


def maxProfitBetterWay(prices: List[int]) -> int:
    res = 0
    lowest = prices[0]

    for price in prices:
        # check it won't go back comparing reversely of the list
        if price < lowest:
            # set min value to buy
            lowest = price
            # get max different (profit) between current price and lowest value
        res = max(res, price - lowest)
    return res

def maxProfitSecondRound(prices: List[int]) -> int:
    buy, profix = 0, 0

    for i in range(len(prices)):
        buy = min(prices[i], buy)
        profix = max(profix, prices[i + 1] - buy)
    return profix


prices = [7,1,5,3,6,4]
print(maxProfit(prices))
print(maxProfitBetterWay(prices))
print(maxProfitSecondRound(prices))

prices = [7,6,4,3,1]
print(maxProfit(prices))
print(maxProfitBetterWay(prices))
print(maxProfitSecondRound(prices))