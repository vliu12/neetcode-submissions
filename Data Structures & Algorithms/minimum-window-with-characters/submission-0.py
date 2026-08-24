class Solution:
    # ideally you must start and end on a character that belongs to t

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        if not t:
            return ""

        counts = {}

        for i in range(len(t)):
            counts[t[i]] = counts.get(t[i], 0) + 1

        # make a frequency map of the letters

        l = 0

        window = {}

        have = 0
        need = len(counts)

        best = (0, float('inf'))

        # s = "OUZODYXAZV", t = "XYZ"

        for r in range(len(s)):
            curr = s[r]

            window[curr] = window.get(curr, 0) + 1
            if curr in counts and window[curr] == counts[curr]:
                have += 1

            while have == need:

                curr_window = r - l + 1
                if curr_window < (best[1] - best[0] + 1 ):
                    best = (l, r)

                left_char = s[l]
                window[left_char] -= 1

                if left_char in counts and window[left_char] < counts[left_char]:
                    have -= 1

                l += 1

        left, right = best

        return s[left : right+1] if best[1] != float('inf') else ""

        




            
            


                
