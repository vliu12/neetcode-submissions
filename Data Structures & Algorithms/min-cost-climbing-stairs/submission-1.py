from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i):
            if i<= 1:
                a = 0
            else:
                a = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])

            return a

        return dp(len(cost))
