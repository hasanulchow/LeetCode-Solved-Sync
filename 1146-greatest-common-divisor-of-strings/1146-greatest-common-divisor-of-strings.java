// class Solution {
//     public String gcdOfStrings(String str1, String str2) {
//         if (!(str1 + str2).equals(str2 + str1))

//         int gcd = gcd(str1.length(), str2.length());
//         return str1.substring(0,gcd);
        
//     }
//     private int gcd(int a, int b) {
//         return b == 0 ? a : gcd(b, a % b);
//     }
// }

class Solution {
    public String gcdOfStrings(String str1, String str2) {
        // Check if str1 + str2 is equal to str2 + str1, which means they can form a common substring
        if (!(str1 + str2).equals(str2 + str1)) {
            return ""; // If not, return an empty string
        }

        // Find the GCD of the lengths of the two strings
        int gcd = gcd(str1.length(), str2.length());
        
        // Return the substring of the first string with length equal to the GCD of the string lengths
        return str1.substring(0, gcd);
    }

    // Helper method to compute the greatest common divisor (GCD)
    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
