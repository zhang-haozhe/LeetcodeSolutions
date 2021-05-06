# 78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

# Result:

Runtime: 24 ms, faster than 98.46% of Python3 online submissions for Subsets.
Memory Usage: 14.5 MB, less than 19.30% of Python3 online submissions for Subsets.

# Solution:

Time complexity: O(n ^ min{k, n-k} \* n)
Space complexity: O(n)

This problem is solved by taking all possible combinations at each level, i.e., taking combinations for 1 number, 2 numbers, then 3 numbers for [1,2,3]. At the end, append [] to the output list.

I believe the time complexity for this question is O(n ^ min{k, n-k} \* n), where n is the length of nums, and k is the number of numbers selected for combination. The time complexity is O(n ^ min{k, n-k}) for combination as defined by itself. In this function, we do n times of combination calculations because n also represents the number of levels.
