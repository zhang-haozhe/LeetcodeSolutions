# 143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

# Result:

Runtime: 68 ms, faster than 100.00% of Python3 online submissions for Reorder List.
Memory Usage: 23.4 MB, less than 18.63% of Python3 online submissions for Reorder List.

# Solution:

Time complexity: O(n)
Space complexity: O(n)

I solved this problem by converting the linked list to a list. Once a list is formed, the head node points to the tail node, and then the tail node points to the head node's next node, so on so forth. At the end, the last node points to None to end the linked list.

Because we create a list to store the linked list, the space complexity is O(n), and since we only traverse through each node one time, the time complexity is also O(n).
