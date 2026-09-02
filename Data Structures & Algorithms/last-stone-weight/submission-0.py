import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            # we want a max heap, so we negate the weights
            heapq.heappush(max_heap, -stone)


        while len(max_heap) > 1:
            x = -(heapq.heappop(max_heap))
            y = -(heapq.heappop(max_heap))

            if x == y:
                print(len(max_heap))
                continue
            
            if x > y:
                new_y = x - y
                heapq.heappush(max_heap, -new_y)

        return -max_heap[0] if max_heap else 0