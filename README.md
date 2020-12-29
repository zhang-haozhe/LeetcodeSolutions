# 98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

# Result:

Runtime: 44 ms, faster than 71.00% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 17.5 MB, less than 5.99% of Python3 online submissions for Validate Binary Search Tree.

# Solution:

Time complexity: O(n)
Space complexity: O(n)

For a BST, the order of in-order traversal is exactly the way to traverse each node by value. If the tree is a valid BST, the values should be incrementing and no duplicates should be found.
