class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Add a leading space to both 'sentence' and 'searchWord' to easily handle edge cases (like matching at the beginning of the sentence)
        s = ' ' + sentence
        t = ' ' + searchWord

        # Find the index of the first occurrence of 'searchWord' as a prefix in the sentence
        m = s.find(t)

        # If 't' (searchWord) is not found in 's' (sentence), return -1
        if m == -1:
            return -1

        # Return the position of the first word that starts with 'searchWord'.
        # We count spaces before the match to determine which word it is in the sentence.
        # We add 1 because the first word starts after the first space.
        return 1 + s[:m].count(' ')
