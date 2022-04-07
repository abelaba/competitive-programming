# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findHeight(self, node):

        if not node:
            return 0
        left = self.findHeight(node.left)
        right = self.findHeight(node.right)

        return max(left, right) + 1

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return

        left = self.findHeight(root.left)
        right = self.findHeight(root.right)

        if left < right:
            return self.lcaDeepestLeaves(root.right)
        elif left > right:
            return self.lcaDeepestLeaves(root.left)
        else:
            return root
