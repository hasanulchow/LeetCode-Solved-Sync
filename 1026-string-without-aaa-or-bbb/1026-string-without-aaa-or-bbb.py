class Solution:
    def strWithout3a3b(self, A, B):
        if(B <= A < 2 * B): return "aab" * (A - B) + "ab" * (2 * B - A);
        elif(2 * B <= A <= 2 * B + 2): return "aab" * B + "a" * (A - B * 2);
        elif(A < B < 2 * A): return "bba" * (B - A) + "ba" * (2 * A - B); 
        elif(2 * A <= B <= 2 * A + 2): return "bba" * A + "b" * (B - A * 2);
        else: return "";