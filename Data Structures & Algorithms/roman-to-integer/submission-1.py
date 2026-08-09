class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I" : 1, "V" : 5, "X": 10, "L":50, 
                "C": 100, "D":500, "M":1000}

        res = 0
        # largest to smallest: add them up
        # if smaller comes before larger, subtract the smaller 

        for i in range(len(s)):
            # bound check + check if curr is smaller than next
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        
        return res