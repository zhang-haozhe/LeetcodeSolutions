# 9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

# Result:

Runtime: 80 ms, faster than 40.78% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 56.77% of Python3 online submissions for Palindrome Number.

# Solution:

This solution does not convert the number from integer to string, as requested. Instead, it directly compares the first and the last digits, the second and the second last digits, so on so forth, to get the final result. The number of comparisons is set to length // 2. The method to get the desired digit is to first divide the number by the nth power of 10, where n is the digit number that is desired. During the comparisons, if any two of the digits do not match, the function returns false.
