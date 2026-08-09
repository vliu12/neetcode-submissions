class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def isPalindrome(s):
            return s == s[::-1]

        length = len(s)
        counter = 0
        
        for i in range(length):
            for j in range(i+1, length+1):
                
                word = s[i:j]
                if isPalindrome(word):
                    counter += 1

        return counter