class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        // Lists to store numbers in three categories
        List<Integer> less = new ArrayList<>();
        List<Integer> equal = new ArrayList<>();
        List<Integer> greater = new ArrayList<>();

        // Categorize numbers
        for (int num : nums) {
            if (num < pivot) {
                less.add(num);
            } else if (num == pivot) {
                equal.add(num);
            } else {
                greater.add(num);
            }
        }

        // Merging lists into a single array
        int[] result = new int[nums.length];
        int index = 0;

        for (int num : less) result[index++] = num;
        for (int num : equal) result[index++] = num;
        for (int num : greater) result[index++] = num;

        return result;
    }
}