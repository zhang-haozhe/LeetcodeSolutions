# 242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

# Result:

Runtime: 44 ms, faster than 84.89% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.3 MB, less than 34.13% of Python3 online submissions for Valid Anagram.

# Solution:

The key is to examine if the numbers of appearances of each character are the same. Hence, a dictionary is the perfect data structure for this solution.
