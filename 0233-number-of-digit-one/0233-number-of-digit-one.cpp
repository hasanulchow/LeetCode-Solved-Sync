class Solution { 
public:
    int countDigitOne(int n) {
        int ret = 0; // Initialize the counter for the total number of '1's

        // Loop through each digit place (units, tens, hundreds, etc.)
        for (long long int i = 1; i <= n; i *= 10) {
            int a = n / i; // `a` is the number of complete groups for the current digit place
            int b = n % i; // `b` is the remainder when dividing by the current digit place
            int x = a % 10; // `x` is the digit at the current place

            if (x == 1) {
                // If the current digit is 1:
                // Count all the 1s contributed by full groups and the partial group (remaining digits + 1)
                ret += (a / 10) * i + (b + 1);
            } else if (x == 0) {
                // If the current digit is 0:
                // Count only the 1s contributed by the full groups
                ret += (a / 10) * i;
            } else {
                // If the current digit is greater than 1:
                // Count all the 1s contributed by the full groups plus one additional group
                ret += (a / 10 + 1) * i;
            }
        }

        return ret; // Return the total count of '1's in all digits from 1 to n
    }
};
