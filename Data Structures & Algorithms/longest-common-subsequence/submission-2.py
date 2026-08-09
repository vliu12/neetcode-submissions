from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(None)
        def dp (i, j):
            if i == 0 or j == 0:
                a = 0
            elif text1[i-1] == text2[j-1]:
                a = 1 + dp(i - 1, j - 1)
            else:
                a = max(dp(i, j-1), dp(i-1,j))
            return a

        return dp (len(text1), len(text2))

        