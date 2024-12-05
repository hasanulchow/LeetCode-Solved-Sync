class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)  # Length of the input strings
        i, j = 0, 0  # Pointers for start and target
        
        # Iterate through both strings
        while i < n or j < n:
            # Skip underscores in start
            while i < n and start[i] == '_':
                i += 1
            
            # Skip underscores in target
            while j < n and target[j] == '_':
                j += 1
            
            # If both pointers reach the end of the strings, break out
            if i == n and j == n:
                break

            # If one of the pointers reaches the end but the other doesn't, it's impossible
            if i == n or j == n:
                return False

            # Compare the characters at both pointers
            if start[i] != target[j]:
                return False

            # Check movement restrictions based on 'L' and 'R'
            if start[i] == 'L' and i < j:  # 'L' should move to the left
                return False
            if start[i] == 'R' and i > j:  # 'R' should move to the right
                return False
            
            # Move both pointers to the next character
            i += 1
            j += 1
        
        # If we exit the loop without issues, the transformation is possible
        return True
