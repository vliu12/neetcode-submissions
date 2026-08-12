class Solution:
    def climbStairs(self, n: int) -> int:
        
        ''' DP[1] = 1 
            DP[i] = DP[i-1] + DP[i-2]
        '''
        

        if n <= 2:
            return n

        memo = [0] * (n+1)

        memo[1] = 1
        memo[2] = 2

        
        for i in range(3, n + 1):
            memo[i] = memo[i-1] + memo[i-2]

        return memo[n]