class Solution:
    # sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:  
        charSet = set()
        l = 0

        res = 0
        
        for r in range(len(s)):
            # removeing all duplicate characters
            while s[r] in charSet:
                # remove leftmost character
                charSet.remove(s[l])
                # update leftmost pointer
                l += 1
            # add rightmost character to set
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res