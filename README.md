# 92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?

# Result:

Runtime: 28 ms, faster than 84.50% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 14.2 MB, less than 89.90% of Python3 online submissions for Reverse Linked List II.

# Solution:

Time complexity: O(n)
Space complexity: O(1)

This solution is not one pass. First, the iterator traverses through the linked list till it finds the two boundaries. Save the node after the right boundary, and then point the next node of the right boundary to none. Then, reverse the list after the left boundary. Once done, point the last node of the finished list to the saved node. If there are nodes before the reversed section, re-link it to the reversed part. If not, set the head to the head of the reversed part.

Since we only traverse through the list at most twice, the time complexity is O(n). We do not create any extra data structure, so the space complexity is O(1).
