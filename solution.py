# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    k = 0
    ans = 0
    def printInorder(self, root):
        
        if root: 
            # First recur on left child 
            self.printInorder(root.left) 

            # then print the data of node 
            self.count += 1
            if self.count == self.k:
                self.ans = root.val
                return

            # now recur on right child 
            self.printInorder(root.right) 
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.printInorder(root)
        return self.ans