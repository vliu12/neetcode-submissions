class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp (i, j):
            if j == 0:
                a = 1
            elif i == 0:
                a = 0
            else:
                coin = coins [i - 1]
                if j < coin:
                    a = dp (i - 1, j)
                else:
                    a = dp (i, j - coin) + dp (i - 1, j)
            return a
        
        return dp (len(coins), amount)
