# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

from typing import List
from math import inf
from math import floor
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
                products.append(left[i-1] * right[i+1])
        return products

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=-inf
        sum=0
        tmp=-inf
        for num in nums:
            sum+=num
            if num <0 or tmp>0:
                tmp=num
            else: 
                tmp+=num

            if tmp>sum:
                sum=tmp
            max_sum=max(max_sum, sum)
        return max_sum

    def maxProduct(self, nums: List[int]) -> int:
        mini = 1
        maxi = 1
        max_sum =- inf
        for num in nums:
            a = mini*num
            b = maxi*num
            mini = min( a, b, num )
            maxi = max( a, b, num )
            max_sum = max( max_sum, maxi )
        return max_sum

    def findMin(self, nums:List[int])->int:
        left=0
        right=len(nums) - 1
        while left != right:
            mid=floor((left+right)/2)
            if nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid 

        return nums[left]

    # def search(self, nums: List[int], target: int) -> int:
    #     left=0
    #     right=len(nums) - 1
        
    #     while left != right:
    #         mid=floor((left+right)/2)

    #         if nums[mid] < target <= nums[right]:
    #             left = mid + 1
    #         elif nums[left] <= target <= nums[mid]:
    #             right = mid
    #         elif  nums[left] < target < target[right] :
    #             break
    #         elif nums[right] < nums[mid] and (target <= nums[right] or nums[mid] < target):
    #             left = mid + 1
    #         elif nums[mid] < nums[left] and (target < nums[mid] or nums[left] < target):
    #             right=mid
            
    #     if nums[left]==target:
    #         return left 
    #     return -1
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_sum = 0
        while left != right:
            area = min(height[left], height[right])* (right-left)
            if height[left]< height[right]:
                left+=1
            else:
                right-=1
            max_sum = max(max_sum, area)
        return max_sum

    def threeSum(self, nums: List[int])-> List[List[int]]:
        nums.sort()
        sums = set()
        for i in range(len(nums)-1):
            left, right = i+1, len(nums)-1
            while left != right:
                if nums[right] + nums[left] + nums[i]> 0:
                    right -= 1
                elif nums[right] + nums[left] + nums[i]< 0:
                    left += 1
                else:
                    if right !=left  and right != i and left != i:
                        sums.add((nums[i], nums[left], nums[right]))
                    right-=1
        return sums

s = Solution()
# s.twoSum([2, 7, 11, 15], 9)
# s.twoSum([3,2,4], 6)
# s.twoSum([3,3], 6)

# s.maxProfit([18,9305,1,8710,2541,9996])

# s.containsDuplicate([1,2,3,1])

# s.productExceptSelf([4,3,2,1,2])
# s.maxSubArray([-2,-1])

# s.maxProduct([3,4,5,1,2])

# s.findMin([2,3,4,5,1])
# s.search([1,3],0)

print(s.threeSum([-1,0,1,2,-1,-4]))
