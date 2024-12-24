class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr :List[int])->int :
            max_ends_here = max_so_far = arr[0]
            for el in arr[1:]:
                max_ends_here = max(el, max_ends_here + el)
                max_so_far = max(max_ends_here, max_so_far )
            return max_so_far
        max_kadane = kadane(nums)  #step1
        totsum = sum(nums)  #step2

        inverted_arr = [-x for x in nums]
        min_kadane = kadane(inverted_arr)  #step3

        if totsum == -min_kadane :  # handle edge case where all 
        #elements in nums are negative.
            return max_kadane

        return max(max_kadane, totsum + min_kadane)  #compare and return max value.            
        