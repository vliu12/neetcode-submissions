class Solution:

    def sumOfSquares(self, n: int) -> int:
        res = 0

        while n != 0:
            x = n % 10
            sq = x ** 2
            res += sq
            n = n // 10

        return res

    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            if n == 1: 
                return True
        
        return False
        
            