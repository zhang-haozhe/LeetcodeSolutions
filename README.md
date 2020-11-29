# 230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example 1:

Input: root = [3,1,4,null,2], k = 1
3
/ \
 1 4
\
 2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
5
/ \
 3 6
/ \
 2 4
/
1
Output: 3

# Result:

Runtime: 48 ms, faster than 75.79% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18 MB, less than 28.74% of Python3 online submissions for Kth Smallest Element in a BST.

# Solution:

According to the property of BST, it is best to traverse the tree inorder. By finding the nth element in the inorder BST, it gives the nth minimum node in the tree.
