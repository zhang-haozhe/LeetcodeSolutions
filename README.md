# 160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

begin to intersect at node c1.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.

# Result:

Runtime: 164 ms, faster than 56.34% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.4 MB, less than 58.02% of Python3 online submissions for Intersection of Two Linked Lists.

# Solution:

Time complexity: O(n \* m)
Space complexity: O(1)

My answer is one of the offcicial solutions to this problem. This approach solves the problem by having one pointer for each start of the linked list. Then, each time, the pointers move towards the common end. If one pointer reaches the end, it is reinitialized at the other head of the linked list. Once these two pointers meet each other, the node is the node where two lists join.

To check if the two lists are not overlapped is easy. Once the first pointer reaches the end of the list, the node is saved as the ending node. When the other pointer also reaches the end, the program compares if the two ends are the same. If not, return None.
