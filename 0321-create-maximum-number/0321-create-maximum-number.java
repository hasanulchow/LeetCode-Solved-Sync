class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        String ans = "";
        // Try all possible splits of `k` between `nums1` and `nums2`
        for (int i = Math.max(0, k - nums2.length); i <= Math.min(nums1.length, k); i++) {
            // Find the maximum sequence of length `i` from `nums1`
            String one = solve(nums1, i);
            // Find the maximum sequence of length `k-i` from `nums2`
            String two = solve(nums2, k - i);
            StringBuilder sb = new StringBuilder();
            int a = 0, b = 0;

            // Merge the two sequences to form the largest number
            while (a < i || b < k - i) {
                // Compare remaining substrings and choose the larger digit
                if (one.substring(a).compareTo(two.substring(b)) >= 0) {
                    sb.append(one.charAt(a++));
                } else {
                    sb.append(two.charAt(b++));
                }
            }

            // Update the answer if the current combination is lexicographically larger
            if (sb.toString().compareTo(ans) > 0) {
                ans = sb.toString();
            }
        }

        // Convert the final result string to an integer array
        int[] res = new int[k];
        for (int i = 0; i < k; ++i) {
            res[i] = ans.charAt(i) - '0';
        }
        return res;
    }

    // Helper function to find the maximum sequence of length `k` from an array
    private String solve(int[] arr, int k) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < arr.length; ++i) {
            // Remove smaller elements from the stack if they can be replaced with larger elements
            // and still leave enough elements for the required sequence
            while (!stack.isEmpty() && arr.length - i + stack.size() > k && stack.peek() < arr[i]) {
                stack.pop();
            }
            // Add the current element to the stack
            stack.push(arr[i]);
        }

        // Build the result string from the top `k` elements of the stack
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
            sb.append(stack.pollLast());
        }
        return sb.toString();
    }
}
