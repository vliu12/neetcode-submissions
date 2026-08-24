from functools import lru_cache

class Solution:
    # so valid numbers are in range 1-26
    # no leading zeroes
    # so basically we have to add whitespace in each slot, with max incr of 2
    # max like "digit size" is 2

    def numDecodings(self, s: str) -> int:
        # solve via DP
        # so at each index, we either add a space or we dont
        # if we adda space, we can go up either 1 or 2 more spaces
        # check validity of the number

        @lru_cache
        def dp(i):
            if i == len(s):
                return 1
            else:
                # if is in range, we can do another call
                # if its out of range, we have to continue
                curr_digit = s[i]

                isValid = False

                if i + 1 < len(s):
                    isValid = True

                if curr_digit == "0":
                    return 0

                ways = dp(i + 1)
                
                if isValid:
                    next_digit = s[i + 1]
                    if int(curr_digit + next_digit) <= 26:
                        ways += dp(i + 2)

                return ways


        ways = dp(0)

        return ways

