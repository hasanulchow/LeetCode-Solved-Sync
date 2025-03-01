class Solution {
    public int[] applyOperations(int[] nums) {
        int[] ans = new int[nums.length];
        if (nums.length == 0) return ans;
        int pointer = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1] && nums[i] != 0) {
                nums[i] *= 2;
                ans[pointer++] = nums[i];
                nums[i + 1] = 0;
            } else if (nums[i] != 0) {
                ans[pointer++] = nums[i];
            }
        }
        if (nums[nums.length - 1] != 0) {
            ans[pointer] = nums[nums.length - 1];
        }
        return ans;
    }
}