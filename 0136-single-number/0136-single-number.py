class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize a variable 'res' to 0, which will hold the result
        res = 0
        
        # Iterate over each number in the input list 'nums'
        for n in nums:
            # Apply the XOR operation between 'n' and 'res'.
            # XORing a number with itself results in 0 (n^n = 0)
            # XORing a number with 0 results in the number itself (0^n = n)
            # This way, pairs of identical numbers will cancel each other out, 
            # and only the unique number will remain in 'res'.
            res = n ^ res
        
        # Return the unique number that doesn't have a pair
        return res
