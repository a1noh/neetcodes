# Link: https://www.youtube.com/watch?v=Y0lT9Fck7qI&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=15
# Title: Climbing Stairs
# Leetcode: https://leetcode.com/problems/climbing-stairs/

def climbStairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n - 1):
        tmp = one
        one = two
        two = tmp + two
    return two
