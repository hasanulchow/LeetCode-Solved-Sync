class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) return "Zero"; // Special case: if the number is 0, return "Zero"
        
        // Strings for large number groups (thousands, millions, billions)
        string bigString[] = {"Thousand", "Million", "Billion"};
        string result = numberToWordsHelper(num % 1000); // Process the first group (units place)
        num /= 1000;

        // Process larger groups (thousands, millions, billions)
        for (int i = 0; i < 3; ++i) {
            if (num > 0 && num % 1000 > 0) { // If the group has a value, convert it to words
                result = numberToWordsHelper(num % 1000) + bigString[i] + " " + result;
            }
            num /= 1000; // Move to the next group
        }

        // Remove any trailing spaces from the result
        return result.empty() ? result : result.substr(0, result.size() - 1);
    }

private:
    string numberToWordsHelper(int num) {
        // Strings for individual digits, teens, and tens
        string digitString[] = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        string teenString[] = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        string tenString[] = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

        string result = "";

        // Handle the hundreds place
        if (num > 99) {
            result += digitString[num / 100] + " Hundred ";
        }
        num %= 100; // Get the remainder after removing the hundreds place

        // Handle numbers in the teens
        if (num < 20 && num > 9) {
            result += teenString[num - 10] + " ";
        } else {
            // Handle the tens place
            if (num >= 20) {
                result += tenString[num / 10] + " ";
            }
            num %= 10; // Get the remainder after removing the tens place

            // Handle the ones place
            if (num > 0) {
                result += digitString[num] + " ";
            }
        }
        
        return result; // Return the result string for this group
    }
};
