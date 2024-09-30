class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        n = len(nums)
        from collections import Counter

        counter = Counter(nums)

        for num , count in counter.items():
            if count > (n // 2) :
                return num
        
        return -1

        # Bruteforce approach : 
        # n = len(nums)
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if nums[j] == nums[i]:
        #             count = count + 1
        #     if count > (n//2) :
        #         return nums[i]        
        # return -1

        # Better  Approach
        # using Hashing 

        # n = len(nums)
        # dict = {}
        # if n < 2 :
        #     return nums[0]
        # else:
        #     for value in nums:
        #         if value in dict.keys():
        #             dict[value] += 1
        #             if dict[value] > (n // 2) :
        #                 return value
        #         else:
        #             dict[value] = 1            
                
            


        




