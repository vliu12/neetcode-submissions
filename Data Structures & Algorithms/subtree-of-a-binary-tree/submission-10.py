# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        val = subRoot.val

        def isEqual(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val: 
                return False
            return isEqual(p.left, q.left) and isEqual(p.right, q.right)

        def checkVal(root, subRoot, val):
            if not root: return False
            if root.val == val and isEqual(root, subRoot):
                return True
            return checkVal(root.left, subRoot, val) or checkVal(root.right, subRoot, val)

        return checkVal(root, subRoot, val)

            