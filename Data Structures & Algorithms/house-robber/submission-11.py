from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        # decision is to rob or not to rob

        # max(nums[i] + DP[i + 2], DP[i + 1])


        @lru_cache
        def dp(i):
            if i >= len(nums):
                return 0

            else:

                return max(nums[i] + dp(i + 2), dp(i + 1))

        return dp(0)