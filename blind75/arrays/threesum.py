# Link: https://www.youtube.com/watch?v=jzZsG8n2R9A&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=9
# Title: Three sum
# Leetcode: https://leetcode.com/problems/3sum/submissions/


def threeSum(nums):
    nums = sorted(nums)
    # print(nums)
    ans = []
    for index, num in enumerate(nums):
        if index > 0 and nums[index] == nums[index - 1]:
            continue
        l, r = index + 1, len(nums) - 1
        while l < r:
            target = nums[l] + nums[r] + num
            if target > 0:
                r = r - 1
            elif target < 0:
                l = l + 1
            else:
                li = [num, nums[l], nums[r]]
                ans.append(li)
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                r -= 1
                l += 1

    return ans
