class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = [set() for _ in range(len(stones))]
        
        # 1st step only 1 move possible of value 1
        dp[0].add(1)
        
        for i in range(1,len(stones)):
            # check all the previous stones from where the jumps are possible
            for j in range(i):
                # store the move value required from jth to ith stone
                diff = stones[i]-stones[j]
                # check if that move value is present in jth stone
                if diff in dp[j]:
                    # If possible, then add possibilities of move values in the ith stone set
                    dp[i].add(diff-1)
                    dp[i].add(diff)
                    dp[i].add(diff+1)
        # If the len of last stone's set is zero, it means no jumps to this stone possible
        return True if len(dp[-1])>0 else False
        