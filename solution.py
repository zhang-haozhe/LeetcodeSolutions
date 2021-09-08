class Solution:
        def exist(self, board: List[List[str]], word: str) -> bool:
            res = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        res = res or self.helper(board, word, i, j)
                        if res:
                            return True
            return False

        def helper(self, board, word, i, j, string="", cnt=0) -> bool:
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return False

            if word[cnt] != board[i][j]:
                return False

            string += board[i][j]

            if string == word:
                return True

            res = False

            # up
            board[i][j] = '*'
            res = res or self.helper(board, word, i - 1, j, string, cnt + 1)

            # down
            res = res or self.helper(board, word, i + 1, j, string, cnt + 1)

            # left
            res = res or self.helper(board, word, i, j - 1, string, cnt + 1)

            # right
            res = res or self.helper(board, word, i, j + 1, string, cnt + 1)
            board[i][j] = word[cnt]

            return res