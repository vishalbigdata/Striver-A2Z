class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        un_ele_arr = []

        for i in nums:
            if i not in un_ele_arr:
                un_ele_arr.append(i)
                

        
        k = len(un_ele_arr)
        j = 0
        for x in un_ele_arr:
            nums[j] = x
            j += 1
        
        

        return k