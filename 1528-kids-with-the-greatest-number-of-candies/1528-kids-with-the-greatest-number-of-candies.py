class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the current maximum number of candies any kid has
        maxCandy = max(candies)
        
        # Initialize an empty list to store the results
        ans = []

        # Loop through each kid's candy count
        for i in range(len(candies)):
            # Check if the current kid will have equal or more than the max if given extraCandies
            ans.append(candies[i] + extraCandies >= maxCandy)
        
        # Return the list of boolean values indicating whether each kid can have the most candies
        return ans
