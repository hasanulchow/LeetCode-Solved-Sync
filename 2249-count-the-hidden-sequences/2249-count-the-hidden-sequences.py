class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        for i in range(1, len(differences)):   
            differences[i] += differences[i-1]
        U, L = max(differences+[0]), min(differences+[0])
        return max(0, 1 + (upper-lower) - (U-L))