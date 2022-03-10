# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, grandChildrenWithEvenGrandParents,):

        if root.left:

            if root.val % 2 == 0:
                if root.left.left:
                    grandChildrenWithEvenGrandParents.append(
                        root.left.left.val)
                if root.left.right:
                    grandChildrenWithEvenGrandParents.append(
                        root.left.right.val)
            left = self.traverse(root.left, grandChildrenWithEvenGrandParents)

        if root.right:

            if root.val % 2 == 0:
                if root.right.left:
                    grandChildrenWithEvenGrandParents.append(
                        root.right.left.val)
                if root.right.right:
                    grandChildrenWithEvenGrandParents.append(
                        root.right.right.val)
            right = self.traverse(
                root.right, grandChildrenWithEvenGrandParents)

    def sumEvenGrandparent(self, root: TreeNode) -> int:

        grandChildrenWithEvenGrandParents = []

        self.traverse(root, grandChildrenWithEvenGrandParents)

        return sum(grandChildrenWithEvenGrandParents)
