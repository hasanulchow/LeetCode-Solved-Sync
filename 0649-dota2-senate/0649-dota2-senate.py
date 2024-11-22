from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Initialize two deques to keep track of the index positions of Radiant ('R') and Dire ('D') senators.
        queue_R = deque()  # Queue for Radiant senators
        queue_D = deque()  # Queue for Dire senators

        # Step 1: Populate the queues with the indices of the Radiant and Dire senators.
        for idx, char in enumerate(senate):
            if char == 'R':
                queue_R.append(idx) 
            elif char == 'D':
                queue_D.append(idx)
        
        # 'next_round_idx' will help simulate the circular nature of the senate. 
        # After each round, the banned senator is "removed", while the senator who bans them gets added back with a new index.
        next_round_idx = len(senate)

        # Step 2: Simulate the voting process in a round-based manner.
        # The process continues until one of the queues becomes empty, meaning one party has no senators left.
        while queue_R and queue_D:
            # Get the first Radiant and Dire senator from their respective queues.
            front_R = queue_R.popleft()
            front_D = queue_D.popleft()

            # Compare their indices:
            # The senator with the smaller index acts first (since they appear earlier in the round).
            if front_R < front_D:
                # Radiant senator bans Dire senator, so Radiant senator remains.
                # The Radiant senator is re-added to the queue with a new index for the next round.
                queue_R.append(next_round_idx)
                next_round_idx += 1  # Increment the index for the next available position
            elif front_D < front_R:
                # Dire senator bans Radiant senator, so Dire senator remains.
                # The Dire senator is re-added to the queue with a new index for the next round.
                queue_D.append(next_round_idx)
                next_round_idx += 1

        # Step 3: Determine the winning party.
        # If there are any Radiant senators left, Radiant wins. Otherwise, Dire wins.
        if queue_R:
            return 'Radiant'
        else:
            return 'Dire'