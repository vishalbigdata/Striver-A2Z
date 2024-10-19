class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashset = {}
        
        for i,num in enumerate(nums):
            if num in hashset.keys() and (i - hashset[num]) <= k:
                return True
            hashset[num] = i
        return False

     

           


        # for  i in range(len(nums)-k):
        #     for j in range(i+1, i+k+1):
        #         if nums[i] == nums[j] :
        #             return True
        # return False



        