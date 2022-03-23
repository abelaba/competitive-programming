# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, index, appearance):
        if not root:
            return

        if index in appearance:
            appearance[index] = max(root.val, appearance[index])
        else:
            appearance[index] = root.val

        if root.left:
            self.dfs(root.left, index + 1, appearance)
        if root.right:
            self.dfs(root.right, index + 1, appearance)

    def bfs(self, root, appearance):

        queue = collections.deque()
        queue.append((root, 0))

        while queue:

            popped, index = queue.popleft()

            if index in appearance:
                appearance[index] = max(popped.val, appearance[index])
            else:
                appearance[index] = popped.val

            if popped.left:
                queue.append((popped.left, index + 1))

            if popped.right:
                queue.append((popped.right, index + 1))

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        appearance = {}

        # self.dfs(root, 0, appearance)
        self.bfs(root, appearance)

        return appearance.values()
