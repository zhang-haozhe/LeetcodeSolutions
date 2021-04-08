# 41. First Missing Positive

Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space?

# Result:

Runtime: 32 ms, faster than 83.96% of Python3 online submissions for First Missing Positive.
Memory Usage: 14.2 MB, less than 75.30% of Python3 online submissions for First Missing Positive.

# Solution:

Time complexity: O(n)
Space complexity: O(n)

I solved this problem by using a map. The point of using a map is to skip sorting.

The first step is to filter out the non-positive elements from the list, because they do not have any impact on the final result.

Then, we take care of the edge cases: if the list is empty, or if it does not start from 1, 1 is the the first missing positive number, so return it.

After this, we set the first missing positive to be the biggest number in the list + 1.

This is when the map comes into play: it associates each number with its next positive number. When traversing through the finished map by key, once a missing number is found, the program compares the stored first missing number and the current missing number and stores the smaller one. Once done, return the smallest missing positive number it has ever found.
