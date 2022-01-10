# Link: https://www.youtube.com/watch?v=UuiTKBwPgAo&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=10
# Title: Container with the most water
# Leetcode: https://leetcode.com/problems/container-with-most-water/submissions/

def maxArea(height) -> int:
    res = 0
    l, r, = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(area, res)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return res