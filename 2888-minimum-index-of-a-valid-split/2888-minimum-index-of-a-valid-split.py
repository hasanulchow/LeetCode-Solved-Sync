class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def find_dominant_element(arr):
            candidate = None
            count = 0
            
            # Boyer-Moore Majority Vote algorithm
            for num in arr:
                if count == 0:
                    candidate = num
                    count = 1
                elif num == candidate:
                    count += 1
                else:
                    count -= 1
            
            count = sum(1 for num in arr if num == candidate)
            return candidate if count > len(arr) // 2 else None

        dominant = find_dominant_element(nums)
        
        if dominant is None:
            return -1
        
        left_count = 0
        total_dominant_count = sum(1 for num in nums if num == dominant)
        
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left_count += 1
            
            left_subarray_count = left_count
            right_subarray_count = total_dominant_count - left_count
            
            if (left_subarray_count > (i + 1) // 2 and 
                right_subarray_count > (len(nums) - i - 1) // 2):
                return i
        
        return -1
        