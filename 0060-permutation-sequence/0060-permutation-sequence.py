"""
Goal: Given two integers `n` and `k`, return the k-th permutation sequence of the numbers 1 to n.
Approach: 
- The key insight is that the problem can be broken down into determining which "block" of permutations the k-th permutation falls into.
- We use factorials to determine the range of permutations for each digit position.
- As we reduce the problem size by one digit at a time, we use the remaining numbers to build the k-th permutation.

Explanation:
1) `nums` stores the numbers from 1 to n.
2) `factorial[i]` stores the factorial of `i` to help determine the number of permutations of `i` elements.
3) The algorithm iteratively picks the correct element for each position by using `k` and the factorials.
4) After choosing the element for a particular position, we update `k` to point to the position in the remaining elements.
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # List of numbers from 1 to n
        nums = [i for i in range(1, n+1)]
        
        # Precompute factorials
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i
        
        # Adjust k to be zero-indexed
        k -= 1
        
        result = []
        for i in range(n-1, -1, -1):
            # Determine the index of the current digit
            index = k // factorial[i]
            
            # Append the digit to the result and remove it from nums
            result.append(str(nums[index]))
            nums.pop(index)
            
            # Update k to point to the position within the smaller set
            k = k % factorial[i]
        
        # Join the result list to form the final permutation string
        return ''.join(result)
