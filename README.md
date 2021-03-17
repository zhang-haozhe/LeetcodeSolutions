# 24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)

# Result:

Runtime: 24 ms, faster than 95.95% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14 MB, less than 99.24% of Python3 online submissions for Swap Nodes in Pairs.

# Solution:

Time complexity: O(n)
Space complexity: O(1)

Declare the pointers first. In edge cases like [] or [1], the try-except block will be triggered and throw "return head" while the right pointer does not have the next node or does not have its value.

Then, the two nodes iterate through the linked list by two steps each time. In each iteration, swap the values of the two nodes.
