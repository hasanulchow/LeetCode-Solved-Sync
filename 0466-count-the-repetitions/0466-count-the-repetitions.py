class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        Determines the maximum number of repetitions of s2 that can be formed 
        using n1 repetitions of s1.

        Args:
        s1 (str): The first string.
        n1 (int): The number of times s1 is repeated.
        s2 (str): The second string.
        n2 (int): The number of times s2 is repeated.

        Returns:
        int: The maximum number of repetitions of s2/n2 that can be formed.
        """
        # Dictionary to store the state (index in s2) and corresponding (s1_round, s2_round)
        start = {}

        # Initialize the count of s1 rounds, s2 rounds, and the index in s2
        s1_round, s2_round, s2_idx = 0, 0, 0

        # Process until all repetitions of s1 are used
        while s1_round < n1:
            s1_round += 1  # Increment the current round of s1

            # Iterate over characters in s1
            for ch in s1:
                # Match characters in s2
                if ch == s2[s2_idx]:
                    s2_idx += 1  # Move to the next character in s2

                    # If s2 is completely matched
                    if s2_idx == len(s2):
                        s2_round += 1  # Increment the count of s2 rounds
                        s2_idx = 0  # Reset the s2 index

            # Check if the current state has been seen before
            if s2_idx in start:
                # Previous state information
                prev_s1_round, prev_s2_round = start[s2_idx]
                
                # Calculate the cycle length for s1 rounds and s2 rounds
                circle_s1_round = s1_round - prev_s1_round
                circle_s2_round = s2_round - prev_s2_round

                # Calculate the remaining s1 rounds after completing full cycles
                res = (n1 - prev_s1_round) // circle_s1_round * circle_s2_round
                left_s1_round = (n1 - prev_s1_round) % circle_s1_round + prev_s1_round

                # Find the corresponding s2 rounds for the leftover s1 rounds
                for key in start:
                    val = start[key]
                    if val[0] == left_s1_round:
                        res += val[1]
                        break

                # Return the total repetitions of s2
                return res // n2
            else:
                # Store the current state (index in s2) with its corresponding round values
                start[s2_idx] = (s1_round, s2_round)

        # Return the total s2 rounds divided by n2 if no cycle is found
        return s2_round // n2
