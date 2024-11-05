class Solution:
    def maxArea(self, height: List[int]) -> int:

        # ans = 0
        # for l in range(len(height)):
        #     for r in range(l+1,len(height)):
        #         ar = (r-l) * min(height[l],height[r])
        #         ans = max(ans, ar)
        # return ans

        # Two Pointer Tchnique

        l = 0
        r = len(height) -1
        ans = 0

        while l< r:
            ar = (r-l) * min(height[l],height[r])
            ans = max(ans, ar)
        
            if height[l] < height[r]:
                l = l+1
            else:
                r = r-1
            
        return ans


        