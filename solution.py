# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        return self.helper(inorder[::-1], postorder[::-1])
    
    def helper(self, inorder: List[int], postorder: List[int]):
        if len(inorder) == 0:
            return None
        head = postorder.pop(0)
        
        headIndex = inorder.index(head)
        
        root = TreeNode(head)
        root.right = self.helper(inorder[:headIndex], postorder)
        root.left = self.helper(inorder[headIndex + 1:], postorder)
        
        return root