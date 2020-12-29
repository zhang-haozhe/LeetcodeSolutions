class Solution:
    def traverse(self, root, arr):
        if root == None:
            return 
        else:
            self.traverse(root.left, arr)
            arr.append(root.val)
            self.traverse(root.right, arr)
            return arr
    def isValidBST(self, root: TreeNode) -> bool:
        array = []
        array = self.traverse(root, array)
        return True if array == sorted(array) and len(array) == len(set(array)) else False