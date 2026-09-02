class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by start, and then do this end
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for (s1, e1) in intervals[1:]:
            last_end = output[-1][1]
            if last_end >= s1:
                output[-1][1] = max(last_end, e1)
            else:
                output.append([s1, e1])

        return output