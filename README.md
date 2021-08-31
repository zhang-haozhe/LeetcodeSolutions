# 41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

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

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

# Result:

Runtime: 916 ms, faster than 53.58% of Python3 online submissions for First Missing Positive.
Memory Usage: 63.9 MB, less than 34.09% of Python3 online submissions for First Missing Positive.

# Solution:

In the first loop, we put values to the slot where they belong to, like putting 5 to the 5th slot, 3 to the 3th slot, etc. During this, we only process values that are between 1~n. Once done, we are left with all the "correct" values in their positions, seperated by values that are out of bound. Then in the second loop, we only need to iterate through the array once again to check if there is a discontinuity. If so, return it. If not, return the maximum number + 1.

# Complexity analysis

Time complexity: O(n)
Space complexity: O(1)

In practice, the first loop is O(n) as it only swaps two values necessarily under the given condition.
Since no other data structure is created, the space complexity is O(1).