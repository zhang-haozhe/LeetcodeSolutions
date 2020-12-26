# 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 \* 104
s consists of English letters, digits, symbols and spaces.

# Result:

Runtime: 56 ms, faster than 81.25% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.4 MB, less than 18.14% of Python3 online submissions for Longest Substring Without Repeating Characters.

# Solution:

Time complexity: O(n)
Space complexity: O(n)

I approached this problem through sliding window. Each time, we test the substring bounded by the left and the right boundaries of the window. During each move, the right boundary moves right by one step and the local maximum is recorded and compared to the global maximum. Each time there is a duplicate element found, the left boundary moves to the next position of the first duplicate element's next position. This means that the program is instead going to examine the substring after the first duplicate element.

However, although this algorithm only contains a while loop that makes the execution in O(n), continuous modifications to the string cause the space to be inefficient. Worst case scenario, the substring could be as long as the entire string, so the complexity is O(n) too.
