# 83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

# Result:

Runtime: 40 ms, faster than 87.83% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.8 MB, less than 67.96% of Python3 online submissions for Remove Duplicates from Sorted List.

# Solution:

We use two pointers to iterate through the linked list. Once the temporary node is not None, the program compares its value with that of its previous node. In case of duplication, the previous node points to the next node of the temporary node. Otherwise, the temporary node goes to the next node and previous node moves to one place before it.
