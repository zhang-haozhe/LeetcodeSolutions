# 978. Longest Turbulent Subarray

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1
 

Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109

# Result:

Runtime: 891 ms, faster than 7.05% of Python3 online submissions for Longest Turbulent Subarray.
Memory Usage: 18.4 MB, less than 97.39% of Python3 online submissions for Longest Turbulent Subarray.

# Solution:

Sliding window. We run the check twice corresponding to the two turbulent array patterns. During each iteration, we check if the current position is larger than or smaller than its previous element, and shift the comparison in the next iteration. If the condition is satisfied, calculate the maximum length of the turbulent array and then move the right boundary right by one. If not met, then start over by moving the left boundary to the position of the right boundary, and then move the right boundary by one.

# Complexity analysis

Time Complexity: O(n)
Space Complexity: O(1)

We run through the array exactly twice, so the time complexity is O(n).
No extra space is created, so the space complexity is O(1).