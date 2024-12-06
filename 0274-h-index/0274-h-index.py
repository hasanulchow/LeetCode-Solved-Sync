class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Determines the h-index of a researcher based on a list of citations.
        The h-index is defined as the largest number `h` such that the researcher has `h` papers 
        with at least `h` citations. This algorithm finds the maximum `h` such that the researcher 
        has at least `h` papers with `h` or more citations.

        The strategy is to:
        1. Sort the list of citations in non-decreasing order.
        2. Iterate over the sorted list to find the largest `h` where the researcher has at least `h` papers with `h` or more citations.
        """

        # Step 1: Sort the list of citations in non-decreasing order.
        citations.sort()

        # `total` is the total number of papers (length of the citations list).
        total = len(citations)

        # Step 2: Iterate through the sorted list of citations.
        for idx, i in enumerate(citations):
            # `h` represents the number of papers that have at least `i` citations.
            h = i

            # Check if the current number of citations (`i`) satisfies the h-index condition.
            # We need `h` papers with `h` or more citations.
            if h >= total - idx:
                # If this condition is met, update `h` and return the result.
                return total - idx

        # If no valid h-index is found, return 0.
        return 0
