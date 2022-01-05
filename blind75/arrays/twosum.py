# Link: https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf
# Title: Two Sum
# Leetcode: https://leetcode.com/problems/two-sum/submissions/


def twoSum(l, target):
    d = {}
    for i in range(len(l)):
        x = target - l[i]
        if x in d:
            return [d[x], i]
        else:
            d[l[i]] = i

    return