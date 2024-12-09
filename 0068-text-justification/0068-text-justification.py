class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Initialize variables
        res = []              # List to store the fully justified lines
        cur = []              # Current line being constructed
        num_of_letters = 0    # Total number of letters in the current line

        # Iterate over each word in the input
        for w in words:
            # Check if adding the current word exceeds the maximum width
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Distribute extra spaces evenly among the words in the current line
                for i in range(maxWidth - num_of_letters):
                    # Add spaces to the words in a cyclic manner
                    cur[i % (len(cur) - 1 or 1)] += ' '

                # Append the justified line to the result
                res.append(''.join(cur))
                # Reset the current line and letter count
                cur, num_of_letters = [], 0

            # Add the current word to the line
            cur += [w]
            num_of_letters += len(w)

        # Handle the last line (left-justified)
        # Add the remaining words and pad the line with spaces to the right
        return res + [' '.join(cur).ljust(maxWidth)]
