# from typing import List

# #1.Two sum
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # This dictionary stores value: index
#         prevMap = {} 

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 # If the complement exists, return the indices
#                 return [prevMap[diff], i]
            
#             # Otherwise, store the current number and its index
#             prevMap[n] = i

# #53.Maximum Subarray
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_total = nums[0]
#         current_sum = nums[0]
        
#         for i in range(1, len(nums)):
#             current_sum = max(nums[i], current_sum + nums[i])
#             max_total = max(max_total, current_sum)
            
#         return max_total
    
# #169.Majority Element
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = None
#         count = 0
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)

#         return candidate