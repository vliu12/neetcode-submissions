class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        count = 1
        
        if not s: return 0
        while right < len(s):
            if s[right] in s[left:right]:
                # count = len(s[left:right])
                print(s[left:right])
                print(right, s[right])
                left +=1
            else:
                right += 1 
                currcount = len(s[left:right])
                count = max(count, currcount)
        
        return count