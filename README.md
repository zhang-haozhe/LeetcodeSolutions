# 105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

# Result:

Runtime: 136 ms, faster than 53.91% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 53 MB, less than 49.83% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

# Solution:

Time complexity: O(n)
Space complexity: O(1)

Because the first element of preorder represents the root of a subtree, each time we pick it as the root and construct a subtree based on it. In inorder, any nodes to its left belong to its left subtree, vice versa. Therefore, in each traversal, we denote a root and delete it from the preorder list, select the left or right subtree nodes from the inorder list and pass down to the next recursive call.

Since we only traverse through each node exactly once, the time complexity is O(n). We are not creating any extra data structure, so the space complexity is O(1).
