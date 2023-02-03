# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, placement,level, root, treeOrder):
        if not root:
            return
        
        treeOrder[placement].append((level, root.val))
        
        self.helper(placement-1, level+1, root.left, treeOrder)
        self.helper(placement+1, level+1, root.right, treeOrder)
		
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        treeOrder = defaultdict(list)
        
        self.helper(0, 0, root, treeOrder)
        
        result = []
        
        for i in sorted(treeOrder.keys()):
            
            values = sorted(treeOrder[i])
            temp = []
            
            for _ , node in values:
                temp.append(node)
            
            result.append(temp)
        
        return result
