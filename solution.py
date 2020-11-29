class Solution:
    def traverse(self, root, stack):
        if root:
            self.traverse(root.left, stack)
            stack.append(root.val)
            self.traverse(root.right, stack)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        self.traverse(root, stack)
        return stack