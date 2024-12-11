class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Initialize a dictionary to store the frequency of each character in magazine
        maga_hash = {}

        # Loop through each character in magazine
        for c in magazine:
            # Update the count of the character in the dictionary
            # If the character is not in the dictionary, start its count at 1
            # Otherwise, increment its current count
            maga_hash[c] = 1 + maga_hash.get(c, 0)

        # Loop through each character in ransomNote
        for c in ransomNote:
            # Check if the character is not in the dictionary 
            # or if its count in the dictionary is 0 (already used up)
            if c not in maga_hash or maga_hash[c] <= 0:
                # If either condition is true, it's impossible to construct ransomNote
                return False
            # Otherwise, decrement the count of the character in the dictionary
            maga_hash[c] -= 1

        # If all characters in ransomNote are successfully matched and used, return True
        return True
