# 23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

# Result:

Runtime: 5883 ms, faster than 5.00% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.1 MB, less than 99.58% of Python3 online submissions for Merge k Sorted Lists.

# Solution:

This solution reduces merging k lists to merging 2 lists (k - 1) times. Each time, we merge the first list with the forthcoming list and then return its head in the end. 

# Complexity analysis

Time Complexity: O(kn)
Space Complexity: O(1)

Merging two list takes O(m + n) time, where m and n are the two lists' length. In this case, we can assume that the length of the first list is constant, and then there are k lists, so it takes O(kn) time in total.