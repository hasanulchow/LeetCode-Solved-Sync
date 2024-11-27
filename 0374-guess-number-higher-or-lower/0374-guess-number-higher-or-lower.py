# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Set initial bounds for the search range: [1, n]
        lowerBound, upperBound = 1, n
        
        # Start with the middle of the range as the first guess
        myGuess = (lowerBound + upperBound) >> 1  # Using bit-shift for efficient division by 2
        
        # Continue guessing until the guess is correct (when guess() returns 0)
        while (res := guess(myGuess)) != 0:
            # If the guess is too high (guess() returns -1), adjust the upper bound
            if res == -1:
                upperBound = myGuess - 1
            # If the guess is too low (guess() returns 1), adjust the lower bound
            elif res == 1:
                lowerBound = myGuess + 1

            # Update the guess to be the middle of the new range
            myGuess = (lowerBound + upperBound) >> 1
        
        # Once we find the correct number (guess() returns 0), return the guess
        return myGuess
