# Link: https://www.youtube.com/watch?v=nIVW4P8b1VA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=7
# Title: Find Minimum in Rotated Sorted Array
# Leetcode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(nums[l], res)
            break

        m = (l + r) // 2
        res = min(nums[m], res)
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res