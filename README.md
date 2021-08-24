# Longest common substring

# Solution

To solve this, we use a 2D array and compare if chars from the two arrays are the same. If yes, then dp[i][j], representing the position at text1[i] and text2[j], is 1 + the length of common subsequence at text1[i - 1] and text2[j - 2].

# Complexity Analysis

Time complexity: O(mn), where m and n represent the lengths of the two strings.
Space complexity: O(mn), same as above.

In order to compare the two strings, an m by n 2D array is created and iterated through.
