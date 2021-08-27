# 331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.

Example 1:

Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: preorder = "1,#"
Output: false
Example 3:

Input: preorder = "9,#,#,1"
Output: false

Constraints:

1 <= preorder.length <= 104
preorder consist of integers in the range [0, 100] and '#' separated by commas ','.

# Result

Runtime: 32 ms, faster than 82.79% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
Memory Usage: 14.2 MB, less than 70.11% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.

# Solution

First, convert the string to an array for easy processing. Then, create a stack to resolve it: each time a node comes in, it is added to the stack with its left and right subtrees being "unresolved", as indicated by False. When a null comes in, it first tries to convert the upper level's left subtree to be "resolved". If it is already resolved, convert the right one to "resolved". In each iteration, check if the uppermost node in the stack has both subtrees resolved, and then pop it if so. In the end, if the stack is empty, return True, otherwise False. During the examination, any exception indicates the serialization is improper so return False.

# Complexity Analysis

Time complexity: O(n)
Space complexity: O(n)

This method queries the string exactly once, so the time complexity is O(n).
To store the string in a structure that makes it easier for processing, an array of size n is created. Then, a stack to verify the serialization is created with size n in the worst case scenario. Therefore, the space complexity is O(n).
