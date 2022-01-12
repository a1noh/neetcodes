# Link: https://www.youtube.com/watch?v=5Km3utixwZs&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=11
# Title: Number of 1 Bits
# Leetcode: https://leetcode.com/problems/number-of-1-bits/

def hammingWeight(self, n: int) -> int:
    # res = 0
    # while n:
    #     res += n % 2
    #     n = n >>1
    # return res

    res = 0
    while n:
        n = n & (n - 1) # Subtract 1 and logic AND on original number - This will allow us to count only "1"s in the bit
        res += 1
    return res