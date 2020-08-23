# 234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

# Result:

Runtime: 84 ms, faster than 47.62% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 23.7 MB, less than 99.65% of Python3 online submissions for Palindrome Linked List.

# Solution:

First note that the definition of ListNode has been modified so that there is now a property of "the last node". The code runs through the linked list, links the nodes to the previous nodes and increments the counter by 1. Once done, it iterates the list for _counter_ times and compares if the two nodes, one starting from the end, going backward, and the other starting from the beginning, going forwards, have the same value. If not, return false.
