class RangeModule:
    def __init__(self):
        # even elements = opens
        # odd elements = closes
        self.X = []

    def bl(self, x):
        # bisect_left: return index i so that all e in X[:i] are e < x
        lo, hi = 0, len(self.X)
        while lo < hi:
            mid = (lo+hi)//2
            if self.X[mid] >= x: hi = mid
            else: lo = mid+1
        return lo

    def br(self, x):
        # bisect_right: return index i so that all e in X[:i] are e > x
        lo, hi = 0, len(self.X)
        while lo < hi:
            mid = (lo+hi)//2
            if self.X[mid] > x: hi = mid
            else: lo = mid+1
        return lo

    def addRange(self, left: int, right: int) -> None:
        i, j = self.bl(left), self.br(right)
        # i is even => not covered by existing range
        self.X[i:j] = [left]*(i%2==0) + [right]*(j%2==0)

    def queryRange(self, left: int, right: int) -> bool:
        i, j = self.br(left), self.bl(right)
        return i==j and (i%2==1)
        

    def removeRange(self, left: int, right: int) -> None:
        i, j = self.bl(left), self.br(right)
        # i is odd => covered by existing range
        self.X[i:j] = [left]*(i%2==1) + [right]*(j%2==1)