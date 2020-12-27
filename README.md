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

Runtime: 68 ms, faster than 74.37% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.4 MB, less than 37.57% of Python3 online submissions for Palindrome Linked List.

# Solution:

Time complexity: O(n)
Space complexity: O(1)

I solved this problem by first reversing the sub-linked list after the middle (the second half). By definition, if the linked list is a palindrome, the first half before the middle point and the reversed second half after the middle point should be identical. Therefore, I locate the middle point and manage to reverse the second half. Then, I compare the two halves in each step.
