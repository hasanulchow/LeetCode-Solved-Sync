class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7
        o0 = ord('0')
        prev = None
        count = 1
        prev_count = 0
        for c in s:
            o = ord(c) - o0

            cur = count if o else 0
            if c == '*':
                cur *= 9
                if prev == '*':
                    cur += prev_count * 15
                elif prev == '1':
                    cur += prev_count * 9
                elif prev == '2':
                    cur += prev_count * 6
            else:
                if prev == '*':
                    if o < 7:
                        cur += 2 * prev_count
                    else:
                        cur += prev_count
                else:
                    if o < 7 and prev == '2':
                        cur += prev_count
                    elif prev == '1':
                        cur += prev_count
            prev_count, count = count, cur % mod
            prev = c
            if not count:
                return 0
        return count