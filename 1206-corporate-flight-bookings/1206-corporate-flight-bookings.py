class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for f, l, s in bookings:
            diff[f - 1] += s
            diff[l] -= s
        for i in range(1, n):
            diff[i] += diff[i - 1]
        return diff[:-1]