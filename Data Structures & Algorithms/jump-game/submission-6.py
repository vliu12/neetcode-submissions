class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # dp(i) whether it is possible to reach the last index starting from index i

        memo = {}

        def dp(i):
            if i >= len(nums)-1:
                return True

            else:
                if i in memo:
                    return memo[i]

                for try_jump in range(1, nums[i] + 1):
                    can_do = dp(i + try_jump)
                    if can_do:
                        memo[i] = True
                        return True
                memo[i] = False
                return False

        can_jump = dp(0)

        return True if can_jump else False