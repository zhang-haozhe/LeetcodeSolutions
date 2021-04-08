# 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up:

Could you solve it in O(n) time complexity and without using division?
Could you solve it with O(1) constant space complexity? (The output array does not count as extra space for space complexity analysis.)

# Result:

Runtime: 248 ms, faster than 39.12% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 22.6 MB, less than 7.37% of Python3 online submissions for Product of Array Except Self.

# Solution:

Time complexity: O(n)
Space complexity: O(n)

The gist to solve this problem is to store the products from left and the products from right. Therefore, we create two arrays to store the products. After that, create an array that stores the products of these two arrays on the corresponding positions.
