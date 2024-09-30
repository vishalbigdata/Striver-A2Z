class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


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
        