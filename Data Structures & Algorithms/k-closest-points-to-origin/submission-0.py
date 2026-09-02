import heapq

class Solution:    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDist(x1, y1, x2, y2):
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            
        kth_closest = []

        for point in points:
            x0 = point[0]
            y0 = point[1]

            dist = getDist(x0, y0, 0, 0)

            heapq.heappush(kth_closest, (-dist, (x0, y0)))

            if len(kth_closest) > k:
                heapq.heappop(kth_closest)

        out = []
        for dst, pt in kth_closest:
            out.append(pt)

        return out
