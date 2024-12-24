class Solution {
public:
    vector<string> ans; // To store all the valid expressions

    vector<string> addOperators(string s, int target) {
        helper(s, target, 0, "", 0, 0); // Start the backtracking process
        return ans;
    }

    void helper(string s, int target, int i, const string& path, long eval, long residual) {
        // Base case: if we've processed the entire string
        if (i == s.length()) {
            if (eval == target) { // Check if the expression evaluates to the target
                ans.push_back(path); // Add the valid expression to the result
                return;
            }
        }

        string currStr; // Current substring being considered
        long num = 0; // Numeric value of the current substring

        // Backtracking loop to explore all substrings starting at position `i`
        for (int j = i; j < s.length(); j++) {
            // Handle cases where a number starts with '0' (e.g., "05" is invalid)
            if (j > i && s[i] == '0') return;

            currStr += s[j]; // Extend the current substring
            num = num * 10 + (s[j] - '0'); // Convert the substring to its numeric value

            // If this is the first number in the expression
            if (i == 0) {
                // Start a new expression with the current number
                helper(s, target, j + 1, path + currStr, num, num);
            } else {
                // Explore the '+' operator
                helper(s, target, j + 1, path + "+" + currStr, eval + num, num);

                // Explore the '-' operator
                helper(s, target, j + 1, path + "-" + currStr, eval - num, -num);

                // Explore the '*' operator
                helper(
                    s, target, j + 1, 
                    path + "*" + currStr, 
                    eval - residual + residual * num, // Adjust evaluation for multiplication
                    residual * num // Update residual for the current number
                );
            }
        }
    }
};
