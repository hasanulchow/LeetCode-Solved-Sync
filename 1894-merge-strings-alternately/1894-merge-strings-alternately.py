class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize pointers for word1 and word2
        i, j = 0, 0

        # Create a list to store the merged result
        res = []

        # Iterate through both words while both have remaining characters
        while i < len(word1) and j < len(word2):
            res.append(word1[i])  # Add character from word1
            res.append(word2[j])  # Add character from word2
            i += 1  # Move pointer for word1
            j += 1  # Move pointer for word2
        
        # Append any remaining characters from word1 (if word1 is longer)
        res.append(word1[i:])
        # Append any remaining characters from word2 (if word2 is longer)
        res.append(word2[j:])
        
        # Join the list of characters into a single string and return
        return "".join(res)
