# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, stack):
        if root:
            self.traverse(root.left, stack)
            self.traverse(root.right, stack)
            stack.append(root.val)
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        self.traverse(root, stack)
        return stack