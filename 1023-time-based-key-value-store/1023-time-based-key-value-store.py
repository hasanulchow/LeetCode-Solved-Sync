from collections import defaultdict 
class TimeMap:

    def __init__(self):
        self.hasho = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hasho[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hasho:
            l, r = 0, len(self.hasho[key])-1

            while l <= r:
                m = (l+r) // 2

                if self.hasho[key][m][1] == timestamp:
                    return self.hasho[key][m][0]
                elif self.hasho[key][m][1] > timestamp:
                    r = m - 1
                else:
                    l = m + 1
                
            if r >= 0: return self.hasho[key][r][0]
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)