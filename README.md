# 104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

# Result:

Runtime: 36 ms, faster than 89.53% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 16.1 MB, less than 23.79% of Python3 online submissions for Minimum Depth of Binary Tree.

# Solution:

This program first determines if the input is empty. If not, then it enters the recursion function. The recursion function iterates through the tree, and when it visits the next level, the level counter increments by one. If there are two children associated to this node, it takes the counter of the child that has a bigger level count.
