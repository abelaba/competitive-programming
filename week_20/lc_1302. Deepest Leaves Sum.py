# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS implementation
    def dfs(self, node, index):
        if not node:
            return

        if index == self.max:
            self.sum += node.val
        elif index > self.max:
            self.sum = node.val

        self.max = max(self.max, index)

        left = self.dfs(node.left, index + 1)
        right = self.dfs(node.right, index + 1)

    def bfs(self, root):
        queue = [(root, 0)]
        maxIndex = 0
        su_m = 0
        while queue:
            node, index = queue.pop()
            if index == maxIndex:
                su_m += node.val
            elif index > maxIndex:
                su_m = node.val

            maxIndex = max(index, maxIndex)
            if node.left:
                queue.append((node.left, index + 1))
            if node.right:
                queue.append((node.right, index + 1))

        return su_m

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # self.sum = 0
        # self.max = 0
        # self.dfs(root, 0)
        # return self.sum
        return self.bfs(root)
