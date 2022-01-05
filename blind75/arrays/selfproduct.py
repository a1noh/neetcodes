# Link: https://www.youtube.com/watch?v=bNvIQI2wAjk&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=4
# Title: Product of array except self
# Leetcode:https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums):
    output = [1] * len(nums)

    pre_fix = 1
    for i in range(len(nums)):
        output[i] = pre_fix
        pre_fix *= nums[i]

    post_fix = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= post_fix
        post_fix *= nums[i]

    print(output)
    return output
