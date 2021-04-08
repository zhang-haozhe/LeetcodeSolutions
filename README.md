# 16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

# Result:

Runtime: 92 ms, faster than 98.11% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.2 MB, less than 88.86% of Python3 online submissions for 3Sum Closest.

# Solution:

Time complexity: O(n^2)
Space complexity: O(1)

A problem very similar to 3 sum. The only difference here is to keep track of the sum with the minimal difference from the target.
