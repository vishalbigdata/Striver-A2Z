class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1 = m-1     # -1
        p2 = n-1    # 0
        pos = m+n-1   # 0

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2] :
                nums1[pos] = nums1[p1]
                p1 -= 1
            else:
                nums1[pos] = nums2[p2]
                p2 -= 1            
            pos = pos - 1

        
        nums1[:p2+1] = nums2[:p2+1]   





        