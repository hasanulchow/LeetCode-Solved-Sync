from math import ceil, log2

class Solution:
    def poorPigs(self, buckets: int, timeDetect: int, timeTest: int) -> int:
        """
        Calculates the minimum number of pigs required to determine the poisoned bucket within the given constraints.
        
        Args:
        buckets (int): The total number of buckets.
        timeDetect (int): The time required to detect if a pig dies after consuming poison.
        timeTest (int): The total time available for testing.
        
        Returns:
        int: The minimum number of pigs required.
        """
        # Calculate the number of tests that can be performed within the total testing time.
        tests = timeTest // timeDetect + 1
        
        # Use the formula derived from the problem:
        # The number of pigs needed is the ceiling of the logarithm (base `tests`) of `buckets`.
        # This can be rewritten using the change of base formula as log2(buckets) / log2(tests).
        return ceil(log2(buckets) / log2(tests))
