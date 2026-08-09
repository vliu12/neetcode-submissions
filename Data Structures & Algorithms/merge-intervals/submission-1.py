class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair : pair[0])

        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            # can merge e.g (1, 3),(2, 4)
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
                # we don't append here, just update lastEnd
            else:
                output.append([start, end])

        return output
