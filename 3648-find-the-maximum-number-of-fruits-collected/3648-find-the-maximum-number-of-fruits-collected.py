class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:   

        @lru_cache(9000)
        def dp(row: int, col: int)-> int:

            if 0 <= col < row < n:                                  
                return fruits[row][col] + max(dp(row-1, col+1),
                                              dp(row  , col+1),
                                              dp(row+1, col+1))
            return 0


        n = len(fruits)
        diag = sum(map(lambda x:fruits[x][x], range(n)))    # <= 1)

        upper = dp(n - 1, 0)                                # <= 2)

        dp.cache_clear()                                    # <= 3)
        fruits = list(zip(*fruits))                         # 
                                                            # 
        lower = dp(n - 1, 0)                                # 

        return diag + upper + lower                         # <= 4)