class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # we want to insert when previous interval has start < curr_s
        # and also when the next interval start is greater, we also wanna merge

        #intervals = [[1,3], [4,6]], newInterval = [2,5]

        start, end = newInterval[0], newInterval[1]

        res = []
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # case that all of the intervals end before the new one starts
        if len(res) == len(intervals):
            intervals.append(newInterval)
            return intervals 

        while i < (len(intervals)) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        res.append(newInterval)

        while i< len(intervals):
            res.append(intervals[i])
            i += 1

        return res


       


        

            


