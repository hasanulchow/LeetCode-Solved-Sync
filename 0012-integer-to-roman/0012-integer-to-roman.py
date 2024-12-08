class Solution:
    def intToRoman(self, num: int) -> str:
        # Step 1: Creating a Dictionary for Lookup
        # The dictionary `num_map` maps integers to their corresponding Roman numeral symbols.
        # It also handles the special subtractive cases like 4 -> "IV" and 9 -> "IX".
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        
        # Step 2: Initialize an empty string `r` to store the resulting Roman numeral.
        r = ''
        
        # Step 3: Iterate over the list of Roman numeral values in descending order.
        # This helps ensure we match the largest possible Roman numeral first.
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # Step 4: Add the Roman numeral symbols corresponding to `n` to `r`
            # as long as `n` is less than or equal to the current `num`.
            # We use a while loop to handle repeated occurrences (e.g., 3 "I"s for 3).
            while n <= num:
                r += num_map[n]  # Add the Roman numeral to the result string `r`.
                num -= n         # Subtract `n` from `num` to reduce the number.
        
        # Step 5: Return the final Roman numeral string.
        return r
