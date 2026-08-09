class Solution:
    # construct a min heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # count the number of times than each num in nums occurs, store it
        # in our dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # min heap construction
        heap = []
        for num in count.keys():
            # push (count[num], num) onto the heap
            heapq.heappush(heap, (count[num], num))
            # if at any point the heap becomes too big, pop it off at root (smallest)
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            # append the num from nums in the tuple (count[num], num)
            res.append(heapq.heappop(heap)[1])

        return res

