class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i):
            if i >= n - 1:
                return 0
            
            ans = float('inf')
            
            for jump in range(1, nums[i] + 1):
                ans = min(ans, 1 + dp(i + jump))
            
            return ans
        
        return dp(0)
