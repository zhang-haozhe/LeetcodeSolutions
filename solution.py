class Solution:        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        head = preorder.pop(0)
        
        headIndex = inorder.index(head)
        
        root = TreeNode(head)
        root.left = self.buildTree(preorder, inorder[:headIndex])
        root.right = self.buildTree(preorder, inorder[headIndex + 1:])
        
        return root
        