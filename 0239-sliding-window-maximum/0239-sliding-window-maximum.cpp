class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res; // Result vector to store the maximum values of each sliding window
        deque<int> deque; // Deque to maintain the elements of the current window in a decreasing order

        for (int idx = 0; idx < nums.size(); idx++) {
            int num = nums[idx];

            // Remove all elements smaller than the current element from the back of the deque
            while (!deque.empty() && deque.back() < num) {
                deque.pop_back();
            }

            // Add the current element to the back of the deque
            deque.push_back(num);

            // Remove the front element from the deque if it's no longer in the current sliding window
            if (idx >= k && nums[idx - k] == deque.front()) {
                deque.pop_front();
            }

            // Add the maximum element (front of deque) to the result once the window is fully formed
            if (idx >= k - 1) {
                res.push_back(deque.front());
            }
        }

        return res; // Return the vector containing the maximums for each sliding window
    }
};
