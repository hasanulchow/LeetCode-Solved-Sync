class SORTracker:

    def __init__(self):
        self.rank = []
        self.i = 0

    def add(self, name: str, score: int) -> None:
        idx = bisect.bisect_left(self.rank, (-score, name))
        self.rank.insert(idx, (-score, name))

    def get(self) -> str:
        self.i += 1
        return self.rank[self.i-1][1] 


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()