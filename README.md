# 33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104

# Result:

Runtime: 36 ms, faster than 92.58% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.8 MB, less than 22.36% of Python3 online submissions for Search in Rotated Sorted Array.

# Solution:

Time complexity: O(log(n))
Space complexity: O(1)

Here is the roadmap to solve the problem:

1. Find out the smallest element in the array. In a shifted sorted array, the smallest element is the pivot that the two subarrays are put together.
2. Conduct binary search within the two subarrays given the position of the pivot, respectively.

Since we only traverse through the list using binary search, the time complexity is O(log(n)). We do not create any extra data structure, so the space complexity is O(1).
