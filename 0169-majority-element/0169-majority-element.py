class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Majority Moore Voting algorithm
        n = len(nums)
        count = 0
        maj_ele = None
        for i in range(n):
            if count == 0:
                count = 1
                maj_ele = nums[i]
            elif maj_ele == nums[i]:
                count +=1
            else:
                count -= 1
        

        # to check
        cnt1 = 0
        for i in range(n):
            if nums[i] == maj_ele:
                cnt1+=1
        
        if cnt1 > (n//2 ) :
            return maj_ele
        else:
            return -1


























        # n = len(nums)
        # from collections import Counter

        # counter = Counter(nums)

        # for num , count in counter.items():
        #     if count > (n // 2) :
        #         return num
        
        # return -1

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
                


        


        




