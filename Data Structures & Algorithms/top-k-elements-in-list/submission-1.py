class Solution:
    # construct a min heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # count the number of times than each num in nums occurs
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

