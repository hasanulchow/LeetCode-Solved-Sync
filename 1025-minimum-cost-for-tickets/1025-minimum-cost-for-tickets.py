from queue import Queue

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last7 = Queue()
        last30 = Queue()
        cost = 0

        for d in days:
            while not last7.empty() and last7.queue[0][0] + 7 <= d:
                last7.get()
            while not last30.empty() and last30.queue[0][0] + 30 <= d:
                last30.get()
            last7.put((d, cost + costs[1]))
            last30.put((d, cost + costs[2]))
            cost = min(cost + costs[0], last7.queue[0][1], last30.queue[0][1])

        return cost