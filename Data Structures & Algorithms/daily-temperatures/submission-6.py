class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] # store temp, index 

        for (i, temp) in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                # this is the case where the temp exceeds on this day
                # we want to store this for future use

                currTemp, currIdx = stack.pop()
                res[currIdx] = i - currIdx # subtract something

            stack.append((temp, i))

        return res

            

