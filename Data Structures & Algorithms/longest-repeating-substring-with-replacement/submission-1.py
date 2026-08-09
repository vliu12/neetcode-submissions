class Solution:
    # sliding window
    def characterReplacement(self, s: str, k: int) -> int: 
        # make counter a dictionary
        count = {}
        l = 0
        res = 0

        maxFreq = 0

        for r in range(len(s)):
            elem = s[r]
            count[elem] = 1 + count.get(elem, 0)

            maxFreq = max(maxFreq, count[elem])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res,  r - l + 1)

        return res
