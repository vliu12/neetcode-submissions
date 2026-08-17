"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # use HASH MAP to map nodes to cloned nodes
        # dfs for all nodes, starting from root?

        cloned = {}

        def dfs(curr):
            if curr in cloned:
                return cloned[curr]

            newNode = Node(curr.val)
            cloned[curr] = newNode

            for nbor in curr.neighbors:
                newNode.neighbors.append(dfs(nbor))

            return newNode

        return dfs(node) if node else None

        

            