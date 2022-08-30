# 212. Word Search II

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109

# Result:

Runtime: 1127 ms, faster than 47.12% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
Memory Usage: 24 MB, less than 32.04% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.

# Solution:

Solved using two deques. This problem is very similar to sliding window maximum, but the difference is that we want to keep track of the sum in order to make it always less than or equal to the limit. Therefore, we use a deque that stores the indices of monotonically incrementing values and one that stores those of monotonically decrementing values. Hence, we can easily retrieve the maximum and the minimum in the sliding window.

Then, if the difference between the two values goes beyond the limit, we move the left bound right and pop the indices that are smaller than the left bound. The remaining values reflect the values that are still in the window. Repeat the last step, until the sum is less than or equal to the limit.

# Complexity analysis

Time complexity: O(N), where N is the number of numbers.
Space Complexity: O(N), where N is the total number of numbers. 

It is easy to understand that it totally takes N time to process N numbers, since in each iteration we only involve appending and popping jobs, which both take O(1) time. In total, we do all of them in O(n) time.

For space, it is O(N) again because the worst case scenario is that the limit is super great, so the two deques have to accomodate all numbers in the list. 