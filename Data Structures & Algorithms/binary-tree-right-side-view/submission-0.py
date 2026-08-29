# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we can bfs level by level
        # on each level, we return only the outermost one, or the one that gets
        # appended last on a run

        if not root:
            return []

        out = []

        q = collections.deque()
        q.append(root)

        while q:
            lenq = len(q)
            level = []

            for i in range(lenq):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            
            if level:
                val = level[-1]
                out.append(val)

        return out
