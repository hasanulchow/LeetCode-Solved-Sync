class Solution {
    public int lengthOfLongestSubstring(String s) {

        int lSubString = 0;
        int subString = 0;
        Set<Character> chars = new HashSet<>();
        for (int i = 0; i < s.length(); i++){
            chars.add(s.charAt(i));
            subString++;
            for (int j = i +1; j<s.length(); j++) {
                if (chars.contains(s.charAt(j))) {
                    break;
                }
                chars.add(s.charAt(j));
                subString++;
            }
            lSubString = Math.max(lSubString, subString);
            subString = 0;
            chars.clear();
        }
        return lSubString;
    }
}