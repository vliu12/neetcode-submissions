# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, curr_max):
            if not node:
                return 0

            good_count = 0

            if node.val >= curr_max:
                good_count += 1
                curr_max = node.val
            
            good_left = dfs(node.left, curr_max)
            good_right = dfs(node.right, curr_max)

            return good_left + good_right + good_count

        return dfs(root, -float('inf'))
            
            