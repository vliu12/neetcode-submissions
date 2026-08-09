class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we know we have n unconnected components to begin with
        # turn into adj list
        adjlist = collections.defaultdict(list)
        for a, b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)
        seen = set()

        # for every edge u add, you remove one connected component so subtract 1
        # for each node, determine how many other nodes are reachable from that node
        # subtract this from the running sum
        def dfs (i):
            nbors = adjlist[i]
            for nbor in nbors:
                if nbor not in seen:
                    seen.add(nbor)
                    dfs(nbor)
            
        
        res = 0
        for node in range(n):
            if node not in seen:
                seen.add(node)
                dfs(node)
                res += 1

        return res
