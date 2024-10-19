class Solution:
    import sys
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]
        current_sum  = nums[0]

        for i in range(1,len(nums)):
            current_sum = max(nums[i],current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


         # apprah 2 
        # n = len(nums)
        # max_sum = float('-inf')

        # for i in range(n):
        #     current_sum = 0
        #     for j in range(i, n):
        #         current_sum += nums[j]
        #         max_sum = max(max_sum, current_sum)

        # return max_sum

        # aprach 1
    
        # n = len(nums)
        # max_sum = float('-inf')  # Initialize to negative infinity

        # for i in range(n):
        #     for j in range(i, n):
        #         current_sum = 0
        #         for k in range(i, j + 1):
        #             current_sum += nums[k]
        #         max_sum = max(max_sum, current_sum)

        # return max_sum

        # optimal Apprach 3 :  kadens Algorithm 
        
        # maxi = -sys.maxsize - 1
        # summ = 0
        # for i in range(len(nums)):
        #     summ = summ + nums[i]
        #     if summ > maxi :
        #         maxi = summ   
        #     if summ < 0 :
        #         summ = 0
        
        # return maxi
        
    