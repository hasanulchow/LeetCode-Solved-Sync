class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        len_n = len(grid[0])
        pf_sum = [[0], [0]]
        
        # prefix sum list of each row
        for r in [0, 1]:
            rs = 0
            for n in grid[r]:
                rs += n
                pf_sum[r].append(rs)

        # loop the perfix sum list record the maximum points the second robot can collect at each index
        points_by_2nd, idx = [], 0
        while idx < len_n:
            tp_2nd = max(pf_sum[0][len_n] - pf_sum[0][idx + 1], pf_sum[1][idx])
            heapq.heappush(points_by_2nd, tp_2nd)
            idx += 1

        return points_by_2nd[0]


        