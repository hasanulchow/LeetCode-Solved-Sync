class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        # Initialize the result array with 1s.
        result = [1] * length
        
        # First pass: Calculate left products and store them in the result array.
        left_product = 1
        for i in range(length):
            result[i] = left_product
            left_product *= nums[i]
        
        # Second pass: Calculate right products and multiply them to the result.
        right_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
