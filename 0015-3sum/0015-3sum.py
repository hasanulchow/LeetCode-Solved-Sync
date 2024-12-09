class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # Initialize the result list to store triplets
        nums.sort()  # Sort the array to facilitate the two-pointer approach

        # Iterate through the array, fixing one number at a time
        for i in range(len(nums)):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers for the remaining two numbers
            j = i + 1  # Left pointer, starting just after the fixed number
            k = len(nums) - 1  # Right pointer, starting at the end of the array

            # Find valid triplets with nums[i] as the fixed number
            while j < k:
                total = nums[i] + nums[j] + nums[k]  # Calculate the sum of the triplet

                if total > 0:  # If the sum is too large, move the right pointer left
                    k -= 1

                elif total < 0:  # If the sum is too small, move the left pointer right
                    j += 1

                else:  # If the sum is zero, it's a valid triplet
                    res.append([nums[i], nums[j], nums[k]])  # Add the triplet to the result
                    j += 1  # Move the left pointer to find the next potential triplet

                    # Skip duplicates for the second number
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return res  # Return the list of all valid triplets
