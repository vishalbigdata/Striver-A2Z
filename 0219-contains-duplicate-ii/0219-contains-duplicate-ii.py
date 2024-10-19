class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashset = {}
        
        for i,num in enumerate(nums):
            if num in hashset.keys() and (i - hashset[num]) <= k:
                return True
            hashset[num] = i
        return False

        