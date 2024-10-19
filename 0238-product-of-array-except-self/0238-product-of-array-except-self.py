class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result  = [1] * n
        # leftproduct / prefix
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product = left_product * nums[i]
        # Right Product
        right_product = 1
        for i in range(n-1,-1,-1):
            result[i] = result[i] * right_product
            right_product = right_product * nums[i]
        return result


        




