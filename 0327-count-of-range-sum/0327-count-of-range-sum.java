class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        int n = nums.length, ans = 0;
        long[] pre = new long[n + 1];
        
        // Calculate prefix sums
        for (int i = 0; i < n; i++) {
            pre[i + 1] = nums[i] + pre[i];
        }
        
        // Sort prefix sums to facilitate binary search
        Arrays.sort(pre);
        int[] bit = new int[pre.length + 2];
        long sum = 0;
        
        // Iterate through the array and count valid range sums
        for (int i = 0; i < n; i++) {
            // Update the BIT with the current sum
            update(bit, bs(sum, pre), 1);
            sum += nums[i];
            
            // Count the range sums that fall within [lower, upper]
            ans += sum(bit, bs(sum - lower, pre)) - sum(bit, bs(sum - upper - 1, pre));
        }
        return ans;
    }

    // Perform binary search to find the index of the first number greater than `sum` in `pre`
    private int bs(long sum, long[] pre) {
        int lo = 0, hi = pre.length;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (pre[mid] > sum) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    // Update the Binary Indexed Tree (BIT) at index `idx` by `inc`
    private void update(int[] bit, int idx, int inc) {
        for (++idx; idx < bit.length; idx += idx & -idx) {
            bit[idx] += inc;
        }
    }

    // Query the sum of elements in the BIT up to index `idx`
    private int sum(int[] bit, int idx) {
        int ans = 0;
        for (++idx; idx > 0; idx -= idx & -idx) {
            ans += bit[idx];
        }
        return ans;
    }
}
