class Solution:
    # Function to calculate the minimum number of candies needed
    def candy(self, ratings: List[int]) -> int:
        # Step 1: Initialize variables
        n = len(ratings)  # Number of children (ratings)
        
        # 'candy' list to store the number of candies each child will receive
        # Initially, assign each child 1 candy
        candy = [1] * n

        # Step 2: Left to right pass to ensure ratings increase get more candies
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:  # If the current child has a higher rating than the previous one
                candy[i] = candy[i - 1] + 1  # Assign 1 more candy than the previous child

        # Step 3: Right to left pass to ensure ratings decrease get more candies
        ans = 0  # Variable to accumulate the total candies
        for i in range(n - 2, -1, -1):  # Start from the second last element and go left
            if ratings[i] > ratings[i + 1]:  # If the current child has a higher rating than the next one
                # Take the max of the current candy and (1 + the candy of the next child)
                candy[i] = max(candy[i], candy[i + 1] + 1)

        # Step 4: Calculate the total candies required
        # Add all values from the candy array to the answer
        ans = sum(candy)

        return ans  # Return the total number of candies
