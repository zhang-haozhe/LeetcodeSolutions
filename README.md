# 1721. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:

Input: head = [1], k = 1
Output: [1]
Example 4:

Input: head = [1,2], k = 1
Output: [2,1]
Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100

# Result:

Runtime: 496 ms, faster than 97.80% of JavaScript online submissions for Swapping Nodes in a Linked List.
Memory Usage: 73.9 MB, less than 81.66% of JavaScript online submissions for Swapping Nodes in a Linked List.

# Solution:

Time complexity: O(n)
Space complexity: O(1)

I solve this problem by first determining the total length of the linked list. Then, traverse through the linked list again to find the two nodes to be swapped. The way to find the two nodes is self-explanatory. Then, swap the two nodes' values.
