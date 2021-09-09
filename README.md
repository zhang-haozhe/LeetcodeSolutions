# 19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

# Result:

Runtime: 40 ms, faster than 22.20% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.4 MB, less than 15.57% of Python3 online submissions for Remove Nth Node From End of List.

# Solution:

Abiding the concept of two pointers, we denote a fast and a slow pointer, where the slow pointer is n steps behind the fast one. It is declared only when the fast one has made n moves towards the end. When fast reaches the end, the slow pointer is exactly pointing to the node being removed. Therefore, we just need to point the previous node's next to the slow's next.

Becasue there can be a case that the head node is removed, we need to set up a dummy head. Then, when returning the head, return its next which is the original head.

# Complexity analysis

Time complexity: O(n)
Space complexity: O(1)

Single pass. The first loop and the second loop only stop when fast reaches the end of the linked list.
Only pointers are created, so the space complexity is O(1).