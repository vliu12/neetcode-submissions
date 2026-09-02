import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_largest = []
        out = []

        for num in nums:
            heapq.heappush(kth_largest, num)

            if len(kth_largest) > k:
                heapq.heappop(kth_largest)

        return kth_largest[0]