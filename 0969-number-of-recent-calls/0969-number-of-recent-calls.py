class RecentCounter:

    def __init__(self):
        self.n=collections.deque()
        

    def ping(self, t: int) -> int:
        self.n.append(t)

        while self.n[0]<t-3000:
            self.n.popleft()

        return len(self.n)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)