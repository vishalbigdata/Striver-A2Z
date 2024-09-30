class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        

        newnums  = list(map(sqr,nums))
        newnums.sort()
        return newnums

def sqr(n):
    return n * n
