class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenating the strings in both orders gives different results,
        # there is no common base string that can construct both.
        if str1 + str2 != str2 + str1:
            return ""

        # Helper function to compute the greatest common divisor (GCD) 
        # of the lengths of the two strings using Euclidean algorithm.
        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        # The GCD of the string lengths tells us the maximum possible length
        # of a string that can be repeated to make both str1 and str2.
        return str1[:gcd(len(str1), len(str2))]
