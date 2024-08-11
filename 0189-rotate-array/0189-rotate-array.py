class Solution:
    def rotate(self, nums: list[int], k: int) -> None:


        k = k % len(nums)


        round = 0
        while round < k :
            
            nums.insert(0,nums[len(nums)-1])
            nums.pop()
            

            round += 1
        
            
        return nums

           