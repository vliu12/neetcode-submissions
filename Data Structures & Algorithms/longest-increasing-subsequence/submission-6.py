from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i == len(nums):
                return 0

            if j == -1 or nums[j] < nums[i]:
                return max(1 + dp(i + 1, i), dp(i + 1, j))

            else:
                return dp(i + 1, j)

        res = dp(0, -1)

        return res 