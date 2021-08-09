# 852. Peak Index in a Mountain Array

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
Example 4:

Input: arr = [3,4,5,1]
Output: 2
Example 5:

Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2

Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.

Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?

# Result:

Runtime: 72 ms, faster than 81.30% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 15.3 MB, less than 57.05% of Python3 online submissions for Peak Index in a Mountain Array.

# Solution:

Time complexity: O(log(n))
Space complexity: O(1)

The way to resolve the problem is to use binary search. During the search, if the current value is larger than the previous value, then we reset the left boundary to the current position to ensure that it starts searching right here. Doing so ensures that the list is incrementing as it moves right too. If the list is not incrementing at the current position, then it sets the right boundary here. Once the two boundaries overlap, return the index of the bigger value of them.

Since we only traverse through the list using binary search, the time complexity is O(log(n)). We do not create any extra data structure, so the space complexity is O(1).
