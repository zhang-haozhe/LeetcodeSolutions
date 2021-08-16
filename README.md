# 876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

# Result

Runtime: 32 ms, faster than 53.04% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.1 MB, less than 90.89% of Python3 online submissions for Middle of the Linked List.

# Solution

Two pointers. We keep track of a slow pointer and a fast pointer, where the slow pointer only moves one step while the fast one moves two. By doing so, we have the progress of the slow pointer half of the fast one, so when the fast one reaches the end, the slow one indicates the middle of the list.

# Complexity Analysis

Time complexity: O(n)
Space complexity: O(1)

The fast pointer goes through the list once, so the time complexity is O(n).
We only use two pointers without creating any new data structures, so the space complexity is O(1).
