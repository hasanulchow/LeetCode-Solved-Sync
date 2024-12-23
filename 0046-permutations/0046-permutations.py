class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: if nums has only one element, return a list containing nums itself
        if len(nums) == 1:
            return [nums[:]]  # Return a copy of the list

        # Initialize the result list to store all permutations
        res = []

        # Iterate through all elements in the nums list
        for _ in range(len(nums)):
            # Pop the first element from the list
            n = nums.pop(0)
            # Recursively find all permutations of the remaining elements
            perms = self.permute(nums)

            # Append the popped element to each of the permutations
            for p in perms:
                p.append(n)

            # Extend the result list with all the permutations obtained
            res.extend(perms)
            # Append the popped element back to the list to restore it for the next iteration
            nums.append(n)
        
        # Return the list of all permutations
        return res
