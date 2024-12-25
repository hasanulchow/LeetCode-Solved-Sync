class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        def merge(left_arr, right_arr):
            # Step 1: Count the index satisfied condition first
            i, j = 0, 0
            # note that i is index of left_arr, j is index of right_arr .
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] > 2 * right_arr[j]:
                    self.count += len(left_arr) - i
                    j += 1
                else:
                    i += 1
            # Step 2: Merge sort left and right
            l, r = 0, 0
            res = []
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] < right_arr[r]:
                    res.append(left_arr[l])
                    l += 1
                else:
                    res.append(right_arr[r])
                    r += 1
            return res + left_arr[l:] + right_arr[r:]
        def divide(arr):
            if len(arr) <= 1: return arr
            # divide the input array into 2 parts
            mid = len(arr)//2
            left_arr = divide(arr[:mid])
            right_arr = divide(arr[mid:])
            return merge(left_arr, right_arr)
        nums = divide(nums)
        return self.count