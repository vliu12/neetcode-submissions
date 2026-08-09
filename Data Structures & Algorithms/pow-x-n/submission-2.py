class Solution:
    def myPow(self, x: float, n: int) -> float:
        def myPowHelper(x, n):
            if x == 0: 
                return 0
            if n == 0:
                return 1
            res = myPowHelper(x, n-1)
        
            return x * res

        if n < 0:
            return 1 / myPowHelper(x, -n)
        else:
            return myPowHelper(x, n)
        