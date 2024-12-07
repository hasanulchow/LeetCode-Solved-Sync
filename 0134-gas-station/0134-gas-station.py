class Solution:
    # Function to find the starting gas station index for a circular route
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Step 1: Check if there is a solution
        if sum(gas) < sum(cost):
            return -1  # If the total gas is less than the total cost, we cannot complete the circuit
        
        # Step 2: Initialize variables
        current_gas = 0  # Tracks the current gas in the tank
        start = 0  # Tracks the index of the possible starting station

        # Step 3: Try to find a valid starting station
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]  # Add gas from station i and subtract the cost to travel to the next station
            if current_gas < 0:  # If at any point current_gas becomes negative, we cannot start from the current station
                current_gas = 0  # Reset the gas to 0, as we can't proceed further from this station
                start = i + 1  # Try the next station as the starting point

        # Step 4: Return the starting station index
        return start
