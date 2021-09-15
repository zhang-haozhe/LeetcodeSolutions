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

Runtime: 1064 ms, faster than 5.04% of Python3 online submissions for Sort List.
Memory Usage: 33.7 MB, less than 26.07% of Python3 online submissions for Sort List.

# Solution:

Time complexity: O(nlogn)
Space complexity: O(1)

This solution solves the problem by the concept of merge sort. Each time, we reduce the list into sublists by seperating it in the middle, until the lists are of length 1 or 2. If the sublist consists of 1 node only, then return it. If the sublist consists of 2, then sort it by comparing the two values and then return it. Therefore, the returned lists become sorted lists. At this moment, we only need to convert the problem to merge two sorted lists multiple times.
