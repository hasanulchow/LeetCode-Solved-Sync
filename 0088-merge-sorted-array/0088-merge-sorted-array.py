from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays, nums1 and nums2, into nums1 in place.
        The first m elements of nums1 represent the actual values, while the rest are zeroed out.
        nums2 has n elements, and the total length of nums1 is m + n after merging.
        
        Time complexity: O(m + n), where m is the number of elements in nums1 and n is the number of elements in nums2.
        Space complexity: O(1), since we modify nums1 in place.
        """
        # Start from the end of nums1, nums2 and the result list (nums1).
        a, b, write_index = m - 1, n - 1, m + n - 1
        
        # While there are still elements in nums2 to merge
        while b >= 0:
            # If nums1 has elements remaining, compare and put the larger one at the write_index
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            # Decrement the write index for the next insertion
            write_index -= 1

        # No need to explicitly return anything since we're modifying nums1 in place.
