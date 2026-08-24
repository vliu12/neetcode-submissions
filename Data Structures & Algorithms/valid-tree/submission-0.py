class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is acyclic, n - 1 edges 
        edge_dict = collections.defaultdict(list)

        for edge in edges:
            edge_dict[edge[0]].append(edge[1])
            edge_dict[edge[1]].append(edge[0])

        visited = set()

        def dfs(node, parent):
            
            visited.add(node)

            for dst in edge_dict[node]:
                if dst == parent:
                    continue
                    
                if dst in visited:
                    return False

                
                visited.add(dst)
                
                if not dfs(dst, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n