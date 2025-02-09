import java.util.HashMap;

class Solution {
    public long countBadPairs(int[] nums) {
        HashMap<Integer, Integer> mp = new HashMap<>(); // Stores frequency of nums[i] - i
        long ans = 0; // Stores the total number of bad pairs
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int r = nums[i] - (i + 1); // Calculate nums[i] - (i + 1)
            mp.put(r, mp.getOrDefault(r, 0) + 1); // Update frequency of r
            ans += (n - i - mp.get(r)); // Add the number of bad pairs involving i
        }

        return ans;
    }
}