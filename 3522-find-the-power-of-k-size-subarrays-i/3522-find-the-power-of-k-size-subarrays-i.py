class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        
        # Iterate over all subarrays of size k
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            
            # Check if the subarray is sorted and contains consecutive integers
            is_consecutive = True
            for j in range(1, k):
                if subarray[j] != subarray[j - 1] + 1:
                    is_consecutive = False
                    break
            
            if is_consecutive:
                result.append(max(subarray))
            else:
                result.append(-1)
        
        return result