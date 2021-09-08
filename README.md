# 79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

# Result:

Runtime: 6466 ms, faster than 52.19% of Python3 online submissions for Word Search.
Memory Usage: 14.3 MB, less than 42.43% of Python3 online submissions for Word Search.

# Solution:

A BFS problem. We first traverse through the board and determine if an element is the same as the first character of the word so we can begin. Once one of such element is found, the helper function begins to run. During each iteration, it queries the four neighboring slots, and see if the next positions have the desired characters. If in this position the next character is found, then search this position's neighboring positions. The visited positions are marked with "*" to indicate they have been visited. Once the search is over, re-assign the original value to it.

# Complexity analysis

Time complexity: O(n * m * 4 ** w), where n * m is the dimension of the grid and w is the length of the word.
Space complexity: O(w)

We are traversing through the entire board in the main function. Then, once needed, we execute the helper function which has a complexity of 4 ** w because for each character in the word, it needs to query four neighboring slots.