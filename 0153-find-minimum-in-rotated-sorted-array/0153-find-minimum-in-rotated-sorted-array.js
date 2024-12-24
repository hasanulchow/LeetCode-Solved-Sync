var findMin = function(nums) {
    let left = 0; // Start pointer
    let right = nums.length - 1; // End pointer

    // Binary search loop
    while (left < right) {
        const mid = Math.floor((left + right) / 2); // Calculate middle index

        // If mid element is less than or equal to the right element,
        // it indicates the smallest element is in the left half (inclusive of mid)
        if (nums[mid] <= nums[right]) {
            right = mid; // Shrink the search range to the left
        } else {
            // Otherwise, the smallest element must be in the right half
            left = mid + 1; // Move the left pointer
        }
    }

    // At the end of the loop, `left` will point to the minimum element
    return nums[left];    
};
