class Solution:
    import sys
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize - 1

        summ = 0

        for i in range(len(nums)):
            summ = summ + nums[i]

            if summ > maxi :
                maxi = summ
            
            if summ < 0 :
                summ = 0
        
        return maxi
        
