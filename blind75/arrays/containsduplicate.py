# Link: https://www.youtube.com/watch?v=3OamzN90kPg&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=3
# Title: Contains Duplicate
# Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def containsDuplicate(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False
