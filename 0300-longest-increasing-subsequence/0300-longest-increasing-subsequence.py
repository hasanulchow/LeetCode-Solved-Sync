class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Finds the length of the longest increasing subsequence (LIS) in a given list of integers.

        Args:
        nums (List[int]): A list of integers.

        Returns:
        int: The length of the longest increasing subsequence.
        """
        res = []  # This list will store the increasing subsequence in a way that helps us find the LIS.

        def binary_search(res, n):
            """
            Performs a binary search to find the index of the smallest element in 'res' that is greater than or equal to 'n'.

            Args:
            res (List[int]): A list representing the current subsequence.
            n (int): The number to search for.

            Returns:
            int: The index of the element in 'res' that is greater than or equal to 'n', or the position where 'n' should be placed.
            """
            left = 0
            right = len(res) - 1

            while left <= right:
                mid = (left + right) // 2
                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left  # This is the position where 'n' should be inserted.

        # Iterate through each number in the input list 'nums'
        for n in nums:
            # If the current number is greater than the last element in 'res', append it to 'res'
            if not res or res[-1] < n:
                res.append(n)
            else:
                # Otherwise, find the index in 'res' where 'n' should replace an existing element
                idx = binary_search(res, n)
                res[idx] = n  # Replace the element at the found index with 'n'
        
        # The length of 'res' gives us the length of the longest increasing subsequence.
        return len(res)
