class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the list `nums` in place by `k` steps to the right.
        - The function modifies the input list `nums` directly, so there is no need to return anything.
        - `k % len(nums)` is used to handle cases where `k` is greater than the length of `nums`, reducing unnecessary rotations.
        """
        
        # If k is larger than the length of nums, we take the modulus to avoid extra rotations.
        # Example: If nums has 5 elements and k = 7, rotating 7 times is the same as rotating 2 times.
        k %= len(nums)

        # Calculate the index `r` where the split should occur.
        # `r` represents the index of the first element that will be moved to the front.
        r = len(nums) - k

        # Create a new list `new` to store the elements from index `0` to `r-1`.
        # These will be the elements that need to be moved to the end of the list.
        new = nums[0:r]

        # Now, we remove the first `r` elements from `nums`, as they will be moved to the end.
        nums[0:r] = []

        # Finally, we append the list `new` to the end of `nums`, completing the rotation.
        nums.extend(new)
