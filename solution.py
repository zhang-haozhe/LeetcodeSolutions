# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.traverse(root, float('-inf'))
    
    def traverse(self, root, biggest):
        if root == None:
            return 0
        biggest = max(biggest, root.val)
        count = 0
        if root.val >= biggest:
            count = 1
        return self.traverse(root.left, biggest) + self.traverse(root.right, biggest) + count