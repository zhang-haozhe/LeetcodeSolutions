# 36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

# Result:

Runtime: 96 ms, faster than 71.15% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14.4 MB, less than 42.52% of Python3 online submissions for Valid Sudoku.

# Solution:

This solution respectively checks if all cells in a row, column and 3x3 subboard are unique.

# Complexity analysis

Time Complexity: O(1)
Space Complexity: O(1)

The time used to check a 9x9 board sudoku's validaty is O(1). Here is how it comes:

1. Check all its rows. A 9x9 board has 9 rows, which is constant.
2. Check all its columns. A 9x9 board has 9 columns, which is constant too.
3. Check all its 3x3 subboards. There are 9 such subboards in a 9x9 board, so the time to run it is still constant.

Also, since we only use a map to check if a number already exists and there are only 0-9, so 10 numbers, the space complexity is still constant. 