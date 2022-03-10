# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque([(root, 0)])
        elements_on_each_level = {}

        while queue:
            popped, level = queue.popleft()

            if level in elements_on_each_level:
                elements_on_each_level[level].append(popped.val)
            else:
                elements_on_each_level[level] = [popped.val]

            if popped.left:
                queue.append((popped.left, level + 1))
            if popped.right:
                queue.append((popped.right, level + 1))

        averages = []
        for index in elements_on_each_level:
            averages.append(
                sum(elements_on_each_level[index])/len(elements_on_each_level[index]))

        return averages
