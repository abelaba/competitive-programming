# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, index, values):
        if not node:
            return
        values[index].append(node.val)

        left = self.dfs(node.left, index + 1, values)
        right = self.dfs(node.right, index + 1, values)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrderTraversal = defaultdict(list)
        self.dfs(root, 0, levelOrderTraversal)

        return levelOrderTraversal.values()
