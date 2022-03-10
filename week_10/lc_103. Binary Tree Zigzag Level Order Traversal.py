# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,root):
        queue = collections.deque([(root,0)])
        elements = {}
        while queue:
            popped, layer = queue.popleft()
            if layer in elements:
                elements[layer].append(popped.val)
            else:
                elements[layer] = [popped.val]
                
            if popped.left:
                queue.append((popped.left,layer + 1))
            if popped.right:
                queue.append((popped.right,layer + 1))
        return elements
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        elements = self.bfs(root)
        zigzag = []
        for i in elements:
            if i % 2 != 0:
                zigzag.append(elements[i][::-1])
            else:
                zigzag.append(elements[i])
                
        return zigzag
                
                
        
        