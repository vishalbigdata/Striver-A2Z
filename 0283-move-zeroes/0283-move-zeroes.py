class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #  not good approach
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.append(nums.pop(i))
        



        #  best and optimal
        j = -1

        # set j pointer to first zero

        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        
        # now j will update if element are ther 
        # if now elemts

        if j == -1:
            return nums
    

        for i in range(j+1, len(nums)):
            if nums[i] != 0:
                # swap
                nums[i], nums[j] = nums[j],nums[i]
                j = j+1
        
        return nums
        
        