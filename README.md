# 1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

# Result

Runtime: 388 ms, faster than 85.37% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 21.9 MB, less than 81.84% of Python3 online submissions for Longest Common Subsequence.

# Solution

To solve this, we use a 2D array and compare if chars from the two arrays are the same. If yes, then dp[i][j], representing the position at text1[i] and text2[j], is 1 + the length of common subsequence at text1[i - 1] and text2[j - 2]. Otherwise, it inherits the length at position text1[i - 1] or text2[j - 1].

# Complexity Analysis

Time complexity: O(mn), where m and n represent the lengths of the two strings.
Space complexity: O(mn), same as above.

In order to compare the two strings, an m by n 2D array is created and iterated through.
