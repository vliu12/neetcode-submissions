# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.res = []
        self.index = 0
        def inord(node):
            if not node:
                return

            inord(node.left)
            self.res.append(node.val)
            inord(node.right)

        inord(root)

    def next(self) -> int:
        val = self.res[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.res)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()