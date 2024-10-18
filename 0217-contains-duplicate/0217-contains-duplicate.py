class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # solution 1
        # return len(nums) != len(set(nums))

        # Solution 2
        hash = {}

        for i,n in enumerate(nums):
            hash[n] = 1 + hash.get(n,0)
            if hash[n] >1 :
                return True
        return False

      
        