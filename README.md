# 106. Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.

# Result:

Runtime: 107 ms, faster than 50.70% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 53.3 MB, less than 32.42% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

# Solution:

Because the first element of the reverse of postorder represents the root of a subtree, each time we pick it as the root and construct a subtree based on it. In inorder, any nodes to its left belong to its left subtree, vice versa. Therefore, in each traversal, we denote a root and delete it from the inorder list, select the left or right subtree nodes from the inorder list and pass down to the next recursive call.

# Complexity analysis

Time complexity: O(n)
Space complexity: O(n)

We build the tree in O(n) time because we repeat the process for each node exactly once.
The space complexity is O(n) because the function call stack is O(n) in the worst case.
