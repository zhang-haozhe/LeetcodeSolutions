# 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

# Result:

Runtime: 32 ms, faster than 63.78% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.2 MB, less than 62.94% of Python3 online submissions for Letter Combinations of a Phone Number.

# Solution:

Time complexity: O(4 ** n!)
Space complexity: O(4 ** n!)

Another variant of the permutation problem. The only difference is that each number is associated with several letters, so I use an array to facilitate querying. 
