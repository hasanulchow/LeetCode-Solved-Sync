class Solution:
    def romanToInt(self, s: str) -> int:
        # Initialize result to 0
        res = 0
        
        # Roman numeral mapping
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Iterate over each pair of consecutive Roman characters
        for a, b in zip(s, s[1:]):
            # If the current numeral is smaller than the next, it's a subtractive case
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]

        # Add the value of the last character
        return res + roman[s[-1]]