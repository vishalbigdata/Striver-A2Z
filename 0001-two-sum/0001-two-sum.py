class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # using to pointer approach
        
        # left = 0
        # right = len(nums) -1

        # while left <= right:
        #     if (nums[left] + nums[right]) == target :
        #         return [left,right]
        #     elif (nums[left] + nums[right]) < target :
        #         left = left + 1
        #     elif (nums[left] + nums[right]) > target :
        #         right = right - 1
            
        # it will not work for a case
        #         nums = [3,2,4]


        # using Hashing 

        viseted = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in viseted:
                return [viseted[complement] , i]
            viseted[num] = i
        
        return []


        


        # numMap = {}
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in numMap:
        #         return [numMap[complement], i]
        #     numMap[num] = i
        # return []
        