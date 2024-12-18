class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Finds the extra character added to string `t` compared to string `s`.

        :param s: str - The original string.
        :param t: str - The string `t` with one extra character.
        :return: str - The extra character in `t`.
        """
        # Calculate the sum of ASCII values of characters in string `s`.
        s_sum = sum(ord(x) for x in s)

        # Calculate the sum of ASCII values of characters in string `t`.
        t_sum = sum(ord(y) for y in t)

        # The difference between the two sums gives the ASCII value of the extra character.
        return chr(t_sum - s_sum)
