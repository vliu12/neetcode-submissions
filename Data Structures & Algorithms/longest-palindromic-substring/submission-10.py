class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(s):
            return s == s[::-1]

        if len(s) == 1:
            return s

        ultMax = ""
        ultLen = 0

        length = len(s)

        for i in range(length):
            for j in range(1, length + 1):
                word = s[i:j]
                if isPalindrome(word) and len(word) > ultLen:
                    ultMax = word
                    ultLen = len(word)

        return ultMax
                
