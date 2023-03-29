from typing import List

""" LeedCode 1365. How Many Numbers Are Smaller Than the Current Number """


class Solution:
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     new_nums = []
    #     for i in range(len(nums)):
    #         cnt = 0
    #         for j in range(len(nums)):
    #             if nums[i] > nums[j]:
    #                 cnt += 1
    #         new_nums.append(cnt)
    #     return new_nums
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(sorted(nums)):
            if num not in hashmap:
                hashmap[num] = ind
        return [hashmap[el] for el in nums]


nums = [8, 1, 2, 2, 3]

s = Solution
print(s.smallerNumbersThanCurrent(s, nums))
