# Time Complexity: O(2 ^ n)
# Space Complexity: O(2 ^ n)
class Solution:
    # The idea is to use BFS to try appending 0 - 9 to each number 
    # starting from a single digit 1 - 9 until the number has n digits
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # init ans
        ans = []
        # push all numbers with single digit to a deque
        # (1, d) : (current position, number)
        d = deque((1, d) for d in range(1, 10))
        # while the queue is not empty
        while d:
            # pop the first element from the deque
            pos, num = d.pop()
            # if the current position is n, 
            if pos == n:
                # then we can append num to ans
                ans.append(num)
            else:
                # otherwise, we can iterate 0 to 9
                for j in range(10):
                    # and use num % 10 to get the last digit of num
                    # then get the difference with j
                    # since (num % 10) - j can be negative and positive
                    # we use abs to cover both case
                    if abs(num % 10 - j) == k:
                        # if the difference is equal to k
                        # we can include digit j 
                        # so multiply the current number by 10 and add j
                        d.append((pos + 1, num * 10 + j))
        # return the final ans
        return ans