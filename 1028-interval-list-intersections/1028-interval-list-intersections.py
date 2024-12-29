class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        M, N = len(firstList), len(secondList)
        i, j = 0, 0

        while i < M and j < N:
            head1, tail1 = firstList[i][0], firstList[i][1]
            head2, tail2 = secondList[j][0], secondList[j][1]

            head = max(head1, head2)
            tail = min(tail1, tail2)

            if head <= tail:
                ans.append([head, tail])
            
            if tail1 < tail2:
                i += 1
            else:
                j += 1
        
        return ans