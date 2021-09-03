# 47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

# Result:

Runtime: 56 ms, faster than 86.04% of Python3 online submissions for Permutations II.
Memory Usage: 14.4 MB, less than 89.99% of Python3 online submissions for Permutations II.

# Solution:

Time complexity: O(n _ n!)
Space complexity: O(n _ n!)

Check out the solution to Permutation I, which is very similar. The only difference is that in each iteration, we only process the first one element if it has duplicates after as noted by "nums[i] == nums[i - 1]". 

In order to know if one element has such duplicates, we need to sort the nums array at the beginning.
