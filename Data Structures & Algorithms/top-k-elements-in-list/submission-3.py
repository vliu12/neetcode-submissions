import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        

        min_heap = []

        for num in counts.keys():
            heapq.heappush(min_heap, (counts[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res


