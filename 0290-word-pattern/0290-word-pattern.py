class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the input string `s` into a list of words
        arr = s.split()
        
        # Check if the length of `pattern` matches the number of words in `arr`
        if len(arr) != len(pattern):
            return False

        # Iterate through each character in `pattern` and its corresponding word in `arr`
        for i in range(len(arr)):
            # Check if the first occurrence index of the current pattern character
            # matches the first occurrence index of the corresponding word
            if pattern.find(pattern[i]) != arr.index(arr[i]):
                return False

        # If all characters and words match the pattern, return True
        return True
