# 18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

# Result:

Runtime: 956 ms, faster than 47.37% of Python3 online submissions for 4Sum.
Memory Usage: 14.2 MB, less than 91.38% of Python3 online submissions for 4Sum.

# Solution:

Time complexity: O(n^3)
Space complexity: O(1)

This is only a more complicated variant of 3 sum. To solve it, we only add pointer b, which is very similar to pointer a that we introduce in 3 sum. It then is just a O(n^2) nested loop set to iterate through each combination of a and b, and then do the same sliding window approach as we do in 3 sum.

The time complexity comes from the 2 nested loops and a while loop for the sliding window for each set of (a, b). Since we dont create any extra data structure, the space complexity is O(1).
