class Solution:
    def removeElement(self, nums, val):
        """
        Removes all occurrences of `val` from the list `nums` in place.
        After the operation, the elements of the list are shifted, and the elements
        remaining in the list (up to the returned length) do not include `val`.
        
        The function returns the new length of the list after removal, which is the number 
        of elements in `nums` that are not equal to `val`.

        Time complexity: O(n), where n is the length of nums, because we traverse the entire list once.
        Space complexity: O(1), since we modify the list in place and do not use extra space.
        """
        
        # `write_index` points to the position where we should write the next valid element.
        write_index = 0
        
        # Traverse each element in the `nums` list using `read_index`.
        for read_index in range(len(nums)):
            # If the current element is not equal to `val`, copy it to `write_index`.
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1  # Increment the write index for the next valid element
        
        # The length of the array after removal of `val` is given by `write_index`,
        # which represents how many elements are left that are not equal to `val`.
        return write_index
