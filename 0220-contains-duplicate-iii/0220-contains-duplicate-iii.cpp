class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        int n = nums.size();  // Get the size of the nums array
        multiset<int> ms;     // Multiset to store window elements in sorted order
        
        int i = 0, j = 0;  // Initialize two pointers for the sliding window
        while (j < n) {
            // Find the first element in the multiset that is greater than nums[j]
            auto up = ms.upper_bound(nums[j]);
            
            // Check if there's a nearby element in the window that satisfies the condition:
            // - The difference between nums[j] and the next element is <= t
            // - The difference between nums[j] and the previous element is <= t
            if ((up != ms.end() && *up - nums[j] <= t) || 
                (up != ms.begin() && nums[j] - *(--up) <= t)) {
                return true; // Return true if an almost duplicate is found
            }
            
            // Insert the current element nums[j] into the multiset
            ms.insert(nums[j]);
            
            // If the window size exceeds k, remove the element at the start of the window
            if (ms.size() == k + 1) {
                ms.erase(nums[i]);  // Remove the element nums[i] from the window
                i++;  // Move the start pointer forward
            }
            
            j++;  // Move the end pointer forward
        }
        return false;  // Return false if no nearby almost duplicate is found
    }
};
