"""Leedcode 2367. Number of Arithmetic Triplets"""
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] + diff in nums and nums[i] + diff * 2 in nums:
                count += 1
        return count


nums = [0, 1, 4, 6, 7, 10]
diff = 3
s = Solution()
print(s.arithmeticTriplets(nums, diff))
