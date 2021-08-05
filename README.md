# 148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

# Result:

Runtime: 176 ms, faster than 91.51% of Python3 online submissions for Sort List.
Memory Usage: 30.3 MB, less than 44.00% of Python3 online submissions for Sort List.

# Solution:

Time complexity: O(nlogn)
Space complexity: O(n)

This is not the most ideal solution because it does not use O(1) space. The way I approach it is to first traverse through the linked list, and then save and sort each node in a list. A linked list is later created from the list and then returned. Since all nodes are saved in a list, the space complexity is O(n), and since the sorting algorithm is the built-in quick sort, the time complexity is O(nlogn).
