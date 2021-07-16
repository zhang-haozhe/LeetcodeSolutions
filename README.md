# 25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz

Follow-up: Can you solve the problem in O(1) extra memory space?

# Result:

Runtime: 44 ms, faster than 92.96% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15 MB, less than 93.01% of Python3 online submissions for Reverse Nodes in k-Group.

# Solution:

Time complexity: O(n)
Space complexity: O(1)

Back-tracking is the key to this problem. We step into the list by every k nodes, and when it reaches the end or when there are less than k nodes at the end, we start to back track. The previous group reverses itself, links to the head of the next node, and then return its head after the reverse.

Since we only traverse through each node once, the time complexity is O(n). We are not creating any extra data structure but just creating nodes, the space complexity is O(1).
