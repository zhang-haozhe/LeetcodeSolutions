# 889. Construct Binary Tree from Preorder and Postorder Traversal

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Example 1:

Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

# Result:

Runtime: 52 ms, faster than 70.55% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
Memory Usage: 14.4 MB, less than 39.31% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.

# Solution:

The recursion runs by telling the function the ranges of the the left subtree and the right subtree. Each time we process a node, we also assign its left and right subtrees.

First, we want to determine the length of the left subtree as denoted by subtracting the left subtree root's index by the right one. The right one's index is exactly one plus the left boundary of the subtree in preorder. The left index is a bit more complex, which is the index, in the preorder list, of the next node of the root in the postorder list, which is the root of the right subtree. Having these two numbers, the left length can be calculated.

The length of the right subtree is much easier to have. It is determined by having the available range minus the left length.

Once done, we only need to pass the parameters to the recursive function to get the subtrees and return the root.

# Complexity analysis

Time complexity: O(n)
Space complexity: O(n)

We build the tree in O(n) time because we repeat the process for each node exactly once.
The space complexity is O(n) because the function call stack is O(n) in the worst case.
