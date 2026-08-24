class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)

        for edge in edges:
            src = edge[0]
            dst = edge[1]

            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()

        components = 0

        def dfs(node):
            visited.add(node)

            for nbor in graph[node]:
                if nbor not in visited:
                    dfs(nbor)

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components

