# Link: https://www.youtube.com/watch?v=WnPLSRLSANE&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=13
# Title: Missing number
# Leetcode: https://leetcode.com/problems/missing-number/

def missingNumber(nums) -> int:
    ans = len(nums)

    for i in range(len(nums)):
        ans += i - nums[i]  # we want to add I (to total sum) but we want to subtract num[i] (to see what value would be left in ans)

    return ans
