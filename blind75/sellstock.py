# Link: https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=2
# Title: Best time to buy and sell stock
# Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def maxProfit(prices) -> int:
    maxP = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r += 1
    return maxP