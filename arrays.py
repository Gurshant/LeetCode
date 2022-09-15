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

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left =0
        right =1
        while(right < len(prices)):
            current_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(max_profit, current_profit)
            else:
                left = right
            right +=1
        return max_profit


    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i, elem in enumerate(nums):
            if elem in s:
                return True
            else:
                s.add(elem)
        return False

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        right = [nums[len(nums)-1]]

        for i in range(1,len(nums)):
            left.append(nums[i] * left[i-1])
            right.insert(0,nums[ len(nums) - i-1] * right[0])
        products=[]

        for i in range(len(nums)):
            if i == len(nums)-1:
                products.append(left[i-1])
            elif i == 0:
                products.append(right[1])
            else:
                a = left[i-1]
                b =right[len(nums)-i-1]
                products.append(left[i-1] * right[i+1])
        return products

s = Solution()
# s.twoSum([2, 7, 11, 15], 9)
# s.twoSum([3,2,4], 6)
# s.twoSum([3,3], 6)

# s.maxProfit([18,9305,1,8710,2541,9996])

# s.containsDuplicate([1,2,3,1])

print(s.productExceptSelf([4,3,2,1,2]))
