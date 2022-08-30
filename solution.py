class Solution:
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            else:
                curr['*'] = word
                
        output = []
        
        def backtrack(i, j, trie, output):
            char = board[i][j]
            curr = trie[char]
            if '*' in curr:
                output.append(curr['*'])
                curr.pop('*')
            board[i][j] = '#'
            
            for _i, _j in self.dirs:
                n_i, n_j = i + _i, j + _j
                if 0 <= n_i < len(board) and 0 <= n_j < len(board[0]) and board[n_i][n_j] in curr:
                    backtrack(n_i, n_j, curr, output)
            if not curr:
                trie.pop(char)
            board[i][j] = char
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    backtrack(i, j, trie, output)
        return output