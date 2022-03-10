# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, sum_, targetSum):
            if root and not root.left and not root.right:
                return sum_ + root.val == targetSum

            if not root:
                return False

            sum_ += root.val

            left = helper(root.left, sum_, targetSum)
            right = helper(root.right, sum_, targetSum)

            return left or right

        return helper(root, 0, targetSum)
