class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = 0  # This will track the current altitude.
        max_altitude = 0  # This will track the highest altitude.
        for i in gain:
            temp += i  # Update the current altitude.
            max_altitude = max(max_altitude, temp)  # Update the max altitude if needed.
        return max_altitude
