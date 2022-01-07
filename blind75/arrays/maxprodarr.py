# Link: https://www.youtube.com/watch?v=lXVy6YWFcRM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=6
# Title: Maximum Product Subarray
# Leetcode: https://leetcode.com/problems/maximum-subarray/

def maxProduct(nums):
    ans = max(nums)
    curMax, curMin = 1, 1
    for i in nums:
        if i == 0:
            curMax, curMin = 1, 1
            continue
        tmp = curMax * i
        curMax = max(curMax * i, curMin * i, i)
        curMin = min(tmp, curMin * i, i)
        ans = max(curMax, curMin, ans)
    return ans