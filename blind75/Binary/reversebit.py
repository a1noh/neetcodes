# Link: https://www.youtube.com/watch?v=UcoN6UjAI64&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=14
# Title: Reversed Bits
# Leetcode: https://leetcode.com/problems/reverse-bits/

def reverseBits(self, n: int) -> int:
    ans = 0
    for i in range(32):
        temp = (n >> i) & 1
        ans = ans | (temp << 31 - i)

    return ans
