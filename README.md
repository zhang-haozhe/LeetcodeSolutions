# 111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

# Result:

Runtime: 552 ms, faster than 48.21% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 53.1 MB, less than 38.04% of Python3 online submissions for Minimum Depth of Binary Tree.

# Solution:

This program first determines if the input is empty. If not, then it enters the recursion function. The recursion function iterates through the tree, and when it visits the next level, the level counter increments by one. If there are two children associated to this node, it takes the counter of the child that has a smaller level count.
