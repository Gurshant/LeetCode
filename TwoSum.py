# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, elem in enumerate(nums):
            if target - elem in dict.keys():
                return [ dict[target - elem],i]
            else:
                dict[elem] = i

s = Solution()
s.twoSum([2, 7, 11, 15], 9)
s.twoSum([3,2,4], 6)
s.twoSum([3,3], 6)
