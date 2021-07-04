# 46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

# Result:

Runtime: 32 ms, faster than 96.63% of Python3 online submissions for Permutations.
Memory Usage: 14.5 MB, less than 41.47% of Python3 online submissions for Permutations.

# Solution:

Time complexity: O(n _ n!)
Space complexity: O(n _ n!)

I solve this question through the divide and conquer approach. The gist of it is to break down the array until the size of the subarray equals 2, so that we can simply return an array of the input array itself and its reverse. Then, getting the two new arrays, the upper-array inserts its first element to any position of the new arrays. By doing this recursively, the problem is solved.
