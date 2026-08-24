from functools import lru_cache

class Solution:

    # sol should include like min(dp(try other coin), try this coin)


    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def dp(i): # min number of coins to make amount i
            min_amt = float('inf')
            if i == 0:
                return 0
            else:
                if i in memo:
                    return memo[i]
                for coin in coins:
                    if i - coin < 0:
                        continue
                    
                    min_amt = min(min_amt, 1 + dp(i - coin))

                    memo[i] = min_amt

            return min_amt

        ans = dp(amount)

        return -1 if ans == float('inf') else ans
        
