class Solution:
    def repeatLimitedString(self, s: str, rl: int) -> str:
        h = [ (-ord(x), y) for x, y in Counter(s).items() ]        
        heapq.heapify(h)
        res = ""

        while h:
            x, y = heapq.heappop(h)
            while y > rl and h: 
                res += chr(-x) * rl
                y -= rl
                a, b = heapq.heappop(h)
                res += chr(-a)
                if (b-1) > 0: heapq.heappush(h, (a, b-1))
            res += chr(-x) * y

        if res:
            i = len(res)-1
            while i >= 0 and res[i] == res[-1]: i -= 1
            if len(res)-i-1 > rl: res = res[:i+1+rl]

        return res