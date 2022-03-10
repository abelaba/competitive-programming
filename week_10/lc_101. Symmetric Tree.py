# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, queue):
        elements = []
        while queue:
            popped, side, parent = queue.popleft()  # popped element
            if elements and elements[-1][2] == parent and elements[-1][0] == popped.val and (elements[-1][1] == "left" and side == "right" or elements[-1][1] == "right" and side == "left"):
                elements.pop()
            else:
                elements.append([popped.val, side, parent])
            if popped.left:
                queue.append((popped.left, "left", popped.val))
            if popped.right:
                queue.append((popped.right, "right", popped.val))

        return len(elements) == 1

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([(root, "root", root.val)])

        return self.bfs(queue)
