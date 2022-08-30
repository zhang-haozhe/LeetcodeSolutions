# 212. Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

# Result:

Runtime: 1788 ms, faster than 62.50% of Python3 online submissions for Word Search II.
Memory Usage: 15.6 MB, less than 73.02% of Python3 online submissions for Word Search II.

# Solution:

DFS + trie. The key here is to use a trie to check if an iterated word is in the words list. If the current word is part of a word in the list, then keep going until it finds the whole word, and delete the '\*' element in the trie to indicate the word has been found and no need to append it to the output list again. One way to optimize the performance of the algo is to delete the current iterator of the trie if it is empty. This can occur when a word has been found and '\*' is removed, which results in an emtpy trie. 

# Complexity analysis

Time complexity: O(M(4 * 3<sup>L-1</sup>)), where M is the number of cells in the board and L is the maximum length of words.
Space Complexity: O(N), where N is the total number of letters in the dictionary.