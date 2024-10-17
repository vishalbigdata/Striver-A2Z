class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 1.  Brteefrce n^2

        # for i in range(len(nums)):
        #     remaining = target - nums[i]
        #     for  j in range(i+1, len(nums)):
        #         if remaining == nums[j]:
        #             return [i, j]
        # return [-1,-1]

                        # or
        # for i in range(len(nums)):
        #     remain = target - nums[i]
        #     if remain in nums[i+1:]:
        #         return [i,nums.index(remain, i+1)]


        # 2.using to pointer approach

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
                # nums = [3,2,4]

        # Oprimal Approahc :  using Hashing 

        hashMap = {}

        for index, value in enumerate(nums):
            reamin  = target - value
            index_of_reamin = hashMap.get(reamin,-1)
            if index_of_reamin != -1 :
                return [index_of_reamin , index]
            hashMap[value] = index



        
