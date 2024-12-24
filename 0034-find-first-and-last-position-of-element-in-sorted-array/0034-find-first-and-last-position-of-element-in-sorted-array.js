/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    // Helper function to perform binary search
    const binarySearch = (nums, target, isSearchingLeft) => {
        let left = 0;
        let right = nums.length - 1;
        let idx = -1; // Initialize the index to -1 to represent not found
      
        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            
            if (nums[mid] > target) {
                right = mid - 1; // Narrow search to the left side
            } else if (nums[mid] < target) {
                left = mid + 1; // Narrow search to the right side
            } else {
                idx = mid; // Target found, store the index
                if (isSearchingLeft) {
                    right = mid - 1; // Continue searching on the left side
                } else {
                    left = mid + 1; // Continue searching on the right side
                }
            }
        }
      
        return idx;
    };
    
    // Find the leftmost index of the target
    const left = binarySearch(nums, target, true);
    // Find the rightmost index of the target
    const right = binarySearch(nums, target, false);
    
    // Return the range as [left, right]
    return [left, right];    
};
