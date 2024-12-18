class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        tsum  = 0
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            l , r = i+1, len(nums) - 1
            while l < r :
                tsum = a + nums[l] + nums[r]
                if tsum > 0 :
                    r -= 1
                elif tsum < 0:
                    l += 1 
                else:
                    ans.append([a,nums[l],nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l< r: 
                        l = l+1
            
        return ans
                        