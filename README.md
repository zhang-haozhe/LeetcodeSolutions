# 31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

# Result:

Runtime: 46 ms, faster than 21.12% of Python3 online submissions for Next Permutation.
Memory Usage: 14.1 MB, less than 93.09% of Python3 online submissions for Next Permutation.

# Solution:

Time complexity: O(n)
Space complexity: O(1)

Counting from right to left, if each digit is larger than or equal to the one to its right, then the number is at its maximum and we only need to flip it.

If one is found smaller than the last digit, then we need to denote it as the destination digit. Then, swap the destination digit and the destination two digit, which is the smallest number that is larger than the destination digit in the digits to the destination digit's right. After the swap, reverse all the digits to the right of the new destination digit (by index). 