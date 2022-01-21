# Link: https://www.youtube.com/watch?v=H9bfqozjoqs&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=16
# Title: Coin Change
# Leetcode: https://leetcode.com/problems/coin-change/


def coinChange(coins, amount) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1
