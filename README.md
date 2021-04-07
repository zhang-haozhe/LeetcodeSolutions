# 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

# Result:

Runtime: 844 ms, faster than 73.87% of Python3 online submissions for 3Sum.
Memory Usage: 17.4 MB, less than 74.05% of Python3 online submissions for 3Sum.

# Solution:

Time complexity: O(n^2)
Space complexity: O(1)

Sliding window/two pointer. First, we can take the solution as comparing the sum of three values in the list, a, b, and c. To solve this problem, the list needs to be sorted. In this solution, we define a as the first one to iterate through the list, b (l) as the left boundary, and c (r) as the right boundary. Since the target that we are looking for is 0, then we only need to shift the boundaries by doing so: if a + b + c > 0, then the right boundary shifts left by one to decrease the total sum, and the left one shifts right vice versa.

Edge cases come in in case of duplicates. Therefore, to avoid duplicates, when changing the values of a and c, we always shift them until they are different from the previous values.
