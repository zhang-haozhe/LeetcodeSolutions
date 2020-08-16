# 82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

# Result:

Runtime: 40 ms, faster than 84.51% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 13.8 MB, less than 74.82% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Solution:

Each time when it encounters a situation that one node and its next node are identical in value, it iterates until it reaches the node when they are no longer equal in value. Then, in case of duplication, the previous node points to the first node in the sequence that has a different value.

There are two edge cases to consider: duplication happening at the beginning and at the end of the list. To get around the first situation, we check if the head's value is equal to the value that should be jumped over. If so, then reset the head to the first node that is not duplicated. In the second situation, as the curr node goes to the end of the list, if it is a duplicated number, then the duplicated part will be jumped over by setting the node before the duplication to point to None.
