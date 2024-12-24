class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        HashMap<String, Integer> wordMap = new HashMap<>();
        Set<Integer> set = new TreeSet<>();
        int n = words.length;
        
        // Step 1: Populate wordMap and set with word indices and lengths.
        for (int i = 0; i < n; i++) {
            wordMap.put(words[i], i);
            set.add(words[i].length());
        }
        
        List<List<Integer>> ans = new ArrayList<>();
        
        // Step 2: For each word in the list, check for possible palindrome pairs.
        for (int i = 0; i < n; i++) {
            int length = words[i].length();
            String reverse = new StringBuilder(words[i]).reverse().toString();
            
            // Check if the reverse of the word exists in the map.
            if (wordMap.containsKey(reverse) && wordMap.get(reverse) != i)
                ans.add(Arrays.asList(i, wordMap.get(reverse)));
            
            // Step 3: Check for palindromic substrings.
            for (Integer k : set) {
                if (k == length)
                    break;
                
                // Check if substring [0, length-k] is a palindrome.
                if (isPalindrome(reverse, 0, length - 1 - k)) {
                    String s1 = reverse.substring(length - k);
                    if (wordMap.containsKey(s1))
                        ans.add(Arrays.asList(i, wordMap.get(s1)));
                }
                
                // Check if substring [k, length-1] is a palindrome.
                if (isPalindrome(reverse, k, length - 1)) {
                    String s2 = reverse.substring(0, k);
                    if (wordMap.containsKey(s2))
                        ans.add(Arrays.asList(wordMap.get(s2), i));
                }
            }
        }
        return ans;
    }
    
    // Helper function to check if a substring is a palindrome.
    private boolean isPalindrome(String s, int left, int right) {
        while (left < right)
            if (s.charAt(left++) != s.charAt(right--))
                return false;
        return true;
    }
}
