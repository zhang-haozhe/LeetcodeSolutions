# 7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# Result:

Runtime: 24 ms, faster than 97.65% of Python3 online submissions for Reverse Integer.
Memory Usage: 14 MB, less than 18.54% of Python3 online submissions for Reverse Integer.

# Solution:

My solution is that each time the program adds one digit times 10 to the power of x to the result variable, where x represents the "reversed place of the digit". For example, given number 123, it adds 1 _ 10 ^ 0, 2 _ 10 ^ 1, and 3 \* 10 ^ 2, respectively. If the number is negative, turn it into a positive number and mark the input as a negative number. When the calculation is completed, the program returns the negative number of the result.
