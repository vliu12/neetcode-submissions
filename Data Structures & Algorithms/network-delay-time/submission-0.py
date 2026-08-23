class Solution:
    
    from collections import heapq
    # djikstras 
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        heap = [(0, k)] # store time, node

        visited = set()


        time = 0

        while heap:
            curr_time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)

            time = curr_time

            for n2, w2 in edges[node]:
                if n2 not in visited:
                    heapq.heappush(heap, (curr_time+w2, n2))

        return time if len(visited) == n else -1

