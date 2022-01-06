# Link: https://www.youtube.com/watch?v=5WZl3MMT0Eg&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=5
# Title: Maximum subarray
# Leetcode: https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    max_sum = nums[0]
    cur_sum = 0
    for i in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += i
        max_sum = max(max_sum, cur_sum)
    return max_sum
