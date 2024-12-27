class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        current = [False] * (len(strs) - 1)  # Track rows that need checking

        for pos in range(len(strs[0])):
            keep = True
            for i in range(1, len(strs)):
                # Check if the previous column was already sorted for this pair
                if not current[i - 1] and strs[i][pos] < strs[i - 1][pos]:
                    count += 1
                    keep = False
                    break
            
            # If we kept this column, update the 'current' state to reflect ties
            if keep:
                for i in range(1, len(strs)):
                    if strs[i][pos] > strs[i - 1][pos]:
                        current[i - 1] = True

        return count
            
                


            

        