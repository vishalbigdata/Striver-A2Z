class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # optimal and better appoach using dynamic array
        if not nums:
            return 0

        # Initialize max_product, min_product, and result with the first element
        max_product = min_product = result = nums[0]
    
        # Iterate over the array starting from the second element
        for num in nums[1:]:
            # Calculate new candidates for max_product and min_product
            temp_max = max(num, max_product * num, min_product * num)
            temp_min = min(num, max_product * num, min_product * num)
            
            # Update max_product and min_product with the computed values
            max_product = temp_max
            min_product = temp_min
            
            # Update the result with the maximum of max_product
            result = max(result, max_product)
    
        return result



        # Bruteforce apprach 
        # n = len(nums)
        # max_product  = float('-inf')
        
        # for i in range(n):
        #     current_product = 1
        #     for j in range(i,n):
        #         current_product *= nums[j]
        #         max_product = max(current_product, max_product)

        # return max_product
