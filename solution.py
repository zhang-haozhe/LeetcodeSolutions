# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, root):
        if root.left != None and root.right == None: 
            return 1 + self.recur(root.left)
        elif root.right != None and root.left == None: 
            return 1 + self.recur(root.right)
        elif root.left == None and root.right == None:
            return 1
        return max(1+self.recur(root.left), 1+self.recur(root.right))
    def maxDepth(self, root: TreeNode) -> int:
        return (0 if root == None else self.recur(root))