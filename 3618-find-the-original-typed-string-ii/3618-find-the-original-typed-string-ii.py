import itertools

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # some heuristics 1
        n = len(word)
        if k == n:
            return 1
        if k > n:
            return 0
        
        groups = []
        for _, it in itertools.groupby(word):
            length = sum(1 for _ in it)
            k -= 1
            if length > 1:
                groups.append(length - 1)
        k = max(0, k)
        
        modulo = 1_000_000_007
        
        answer = 1
        for elem in groups:
            answer = (answer * (elem + 1)) % modulo
        
        # some heuristics 2
        if k == 0:
            return answer
        if k == 1:
            return (answer - 1) % modulo
        if k == 2:
            return (answer - 1 - len(groups)) % modulo
        
        prev_dp = [0] * k
        prev_dp[0] = 1

        for group_size in groups:
            dp = [0] * k
            window_sum = 0
            for prev_cnt, prev_number in enumerate(prev_dp):
                window_sum += prev_number
                if prev_cnt - group_size - 1 >= 0:
                    window_sum -= prev_dp[prev_cnt - group_size - 1]
                window_sum %= modulo
                dp[prev_cnt] = window_sum
            prev_dp = dp
        
        return (answer - sum(prev_dp)) % modulo