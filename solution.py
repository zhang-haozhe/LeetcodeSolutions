# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        rightTree = root.right
        root.right = root.left
        root.left = None
        temp = root
        while temp.right != None:
            temp = temp.right
        temp.right = rightTree