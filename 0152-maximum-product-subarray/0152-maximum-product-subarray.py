class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]
            
            temp_max = max(current, current * max_product, current * min_product)
            min_product = min(current, current * max_product, current * min_product)
            
            max_product = temp_max
            global_max = max(global_max, max_product)
        
        return global_max