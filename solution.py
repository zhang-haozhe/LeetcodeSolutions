# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return [0, -float('inf')]
        
        rightRes = self.helper(root.right)
        leftRes = self.helper(root.left)
        
        maxSingle = max(rightRes[0], leftRes[0], 0) 
        maxTotal = max(rightRes[0] + leftRes[0] + root.val, leftRes[0] + root.val, \
                       rightRes[0] + root.val, rightRes[1], leftRes[1], root.val)
        
        return [maxSingle + root.val, maxTotal]
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[1]
    