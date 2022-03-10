# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    tiltSum = 0

    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)

        right = self.traverse(root.right)

        self.tiltSum += abs(left-right)

        return left + right + root.val

    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.traverse(root)
        return self.tiltSum
