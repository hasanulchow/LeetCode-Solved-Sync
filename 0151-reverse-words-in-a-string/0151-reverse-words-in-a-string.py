class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the input string by spaces into a list of words
        arr = s.split()
        
        # Step 2: Initialize an empty list to store the reversed words
        res = []
        
        # Step 3: Loop through the list of words in reverse order
        for i in range(len(arr) - 1, -1, -1):
            # Append each word to the result list in reverse order
            res.append(arr[i])
        
        # Step 4: Join the words in the result list into a string with spaces between them
        return ' '.join(res)

        