class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if the input string 's' can be segmented into a space-separated 
        sequence of one or more dictionary words.

        Args:
        s (str): The input string to be segmented.
        wordDict (List[str]): The list of words available in the dictionary.

        Returns:
        bool: True if the string can be segmented, False otherwise.
        """
        
        def construct(current, wordDict, memo={}):
            """
            Recursive helper function to check if a string can be segmented
            using the words in the dictionary.

            Args:
            current (str): The current substring being processed.
            wordDict (List[str]): The list of words in the dictionary.
            memo (dict): A dictionary to store already computed results for substrings.

            Returns:
            bool: True if the substring can be segmented, False otherwise.
            """
            # Check if the result for the current substring is already in the memo
            if current in memo:
                return memo[current]

            # Base case: if the current string is empty, segmentation is successful
            if not current:
                return True

            # Check each word in the dictionary
            for word in wordDict:
                # If the current string starts with the dictionary word
                if current.startswith(word):
                    # Remove the word from the start of the string
                    new_current = current[len(word):]
                    # Recursively check the remaining string
                    if construct(new_current, wordDict, memo):
                        # If successful, store the result in the memo and return True
                        memo[current] = True
                        return True

            # If no valid segmentation found, store False in the memo and return
            memo[current] = False
            return False

        # Start the recursive process with the full input string
        return construct(s, wordDict)
