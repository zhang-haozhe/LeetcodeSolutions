# 1189. Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.

# Result:

Runtime: 32 ms, faster than 78.37% of Python3 online submissions for Maximum Number of Balloons.
Memory Usage: 14.3 MB, less than 52.86% of Python3 online submissions for Maximum Number of Balloons.

# Solution:

Count the frequency of each "balloon letter", then divide the frequencies for l and o by two because they present twice in "balloon". Return the frequency of the least frequent letter.

# Complexity analysis

Time Complexity: O(n)
Space Complexity: O(n)

