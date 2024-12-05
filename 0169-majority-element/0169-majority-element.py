class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize a dictionary 'hash' to store the frequency of each number.
        # 'res' will store the number with the highest frequency, and 'majority' 
        # will keep track of the highest frequency found so far.
        hash = {}
        res = majority = 0

        # Loop through each number 'n' in the list 'nums'.
        for n in nums:
            # For each number 'n', increment its count in the 'hash' dictionary.
            # If the number is not in the dictionary, 'get(n, 0)' returns 0, so we add 1 to it.
            hash[n] = 1 + hash.get(n, 0)

            # If the count of 'n' exceeds the current 'majority', update 'res' and 'majority'.
            # 'res' will store the number with the maximum frequency, and 'majority' will
            # store that frequency.
            if hash[n] > majority:
                res = n
                majority = hash[n]

        # After processing all elements, 'res' holds the majority element.
        return res
