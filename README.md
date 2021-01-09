# 114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1

/ \
 2 5
/ \ \
3 4 6
The flattened tree should look like:

1
\
 2
\
 3
\
 4
\
 5
\
 6

# Result:

Runtime: 36 ms, faster than 76.58% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.1 MB, less than 73.99% of Python3 online submissions for Flatten Binary Tree to Linked List.

# Solution:

Time complexity: O(n)
Space complexity: O(h), where h is the height of the tree

My solution approaches the problem by using the preorder traversal. Each time the cursor goes to a node, it makes the left tree the right tree, while the right tree attached to the end of the new right tree.
