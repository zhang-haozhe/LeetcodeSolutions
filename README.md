# 43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

# Result:

Runtime: 168 ms, faster than 24.36% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.2 MB, less than 56.28% of Python3 online submissions for Multiply Strings.

# Solution:

Imagine how you perform multiplication by hand. In multiplication, we multiply each digit from right to left, and thus we reverse the two strings to facilitate iteration. Then, during each multiplication, we multiply the two numbers and then add the carry over. With the result, we can add that to the position in the dp array that reflects the digit of the result. Once one level of iteration is over, add the carry over to the next digit.

Once the calculation is over, we should get an array of number. Use list(map(str, dp)) to convert the int array into a string array and then a string through join.There could be redundant 0s at the beginning of the string, so use lstrip to strip them off from the start.

# Complexity analysis

Time Complexity: O(m*n)
Space Complexity: O(m + n)

