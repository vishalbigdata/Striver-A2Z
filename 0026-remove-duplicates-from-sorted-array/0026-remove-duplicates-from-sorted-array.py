class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        # optimal

        i = 0

        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j] 
                i = i+1
        
        return i+1




        # brute force

    
        # un_ele_arr = []

        # for i in nums:
        #     if i not in un_ele_arr:
        #         un_ele_arr.append(i)
                

        
        # k = len(un_ele_arr)
        # j = 0
        # for x in un_ele_arr:
        #     nums[j] = x
        #     j += 1
        
        

        # return k