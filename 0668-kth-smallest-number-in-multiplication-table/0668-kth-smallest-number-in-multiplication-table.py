class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        Given parameters m and n which define an m * n
        multiplication table, and a parameter k, this program
        uses binary search to find the kth smallest element
        in the table.

        :param m: height (rows) in multiplication table
        :type m: int
        :param n: length (columns in multiplication table
        :type n: int
        :param k: value used to identify kth smallest value
                  in multiplication table
        :type k: int
        :return: kth smallest value from multiplication table
        :rtype: int
        """

        def enough(kth_value) -> bool:
            """
            This method determines whether the given candidate
            value (kth_value) is the kth or higher smallest
            value in the multiplication table.

            :param kth_value: candidate kth smallest value from
                              multiplication table
            :type kth_value: int
            :return: True if kth_value is kth or higher smallest
                     value from multiplication table
            :rtype: bool
            """
            k_count = 0
            for row in range(1, m + 1):
                k_inc = kth_value // row
                if k_inc > n:
                    k_inc = n
                k_count += k_inc
            return k_count >= k

        """
        Binary Search
        """
        left = 1
        right = m * n
        while left < right:
            mid = left + (right - left) // 2
            if enough( mid ):
                right = mid
            else:
                left = mid + 1
        return left