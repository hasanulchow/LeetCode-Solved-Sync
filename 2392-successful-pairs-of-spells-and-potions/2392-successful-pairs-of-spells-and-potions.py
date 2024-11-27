from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Get the number of spells and potions
        n = len(spells)
        m = len(potions)
        
        # Initialize a list to store the result for each spell (the number of successful pairs)
        pairs = [0] * n
        
        # Sort the potions list to enable binary search
        potions.sort()

        # Iterate through each spell
        for i in range(n):
            low = 0
            high = m  # high is the length of the potions list

            # Perform binary search to find the smallest potion that when multiplied by the spell
            # results in a value greater than or equal to the success threshold
            while low < high:
                mid = (low + high) // 2  # Calculate the midpoint index
                # Check if the current spell multiplied by the potion at the midpoint is >= success
                if spells[i] * potions[mid] >= success:
                    # If successful, it means all potions from mid to the end are successful
                    pairs[i] += (high - mid)  # All potions from mid to high will form successful pairs with this spell
                    high = mid  # Move the upper bound to search the left half
                else:
                    # If the current potion doesn't meet the success threshold, search the right half
                    if low == mid:  # If low and mid are the same, we've reached the smallest valid index
                        break
                    low = mid  # Move the lower bound to search the right half

        return pairs  # Return the final list of successful pairs for each spell
