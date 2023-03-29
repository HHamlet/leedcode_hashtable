from typing import List
""" Leedcode 1512. Number of Good Pairs"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        cnt = 0
        for i, el in enumerate(nums):
            hashmap[i] = el
        for k, v in hashmap.items():
            for i in range(len(nums)):
                if v == nums[i] and k < i:
                    cnt += 1
        return cnt


nums = [1, 1, 1, 1]
s = Solution
print(s.numIdenticalPairs(s, nums))
