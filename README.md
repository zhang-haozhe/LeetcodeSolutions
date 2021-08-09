# 162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

# Result:

Runtime: 44 ms, faster than 79.09% of Python3 online submissions for Find Peak Element.
Memory Usage: 14.3 MB, less than 73.01% of Python3 online submissions for Find Peak Element.

# Solution:

Time complexity: O(log(n))
Space complexity: O(1)

The way to resolve the problem is to use binary search. During the search, if the current value is larger than the previous value, then we reset the left boundary to the current position to ensure that it starts searching right here. Doing so ensures that the list is incrementing as it moves right too. If the list is not incrementing at the current position, then it sets the right boundary here. Once the two boundaries overlap, return the index of the bigger value of them.

Since we only traverse through the list using binary search, the time complexity is O(log(n)). We do not create any extra data structure, so the space complexity is O(1).
