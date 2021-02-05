from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
 
        matrix = []
        for _ in range(len(grid) + 1):
            matrix.append([0] * (len(grid[0]) + 1))

        for x in range(1, len(matrix)):
            for y in range(1, len(matrix[0])):
                if x != 1 and y != 1:
                    matrix[x][y] = grid[x - 1][y - 1] + min(matrix[x - 1][y], matrix[x][y - 1])
                elif x == 1 and y != 1:
                    matrix[x][y] = grid[x - 1][y - 1] +  matrix[x][y - 1]
                elif x != 1 and y == 1:
                    matrix[x][y] = grid[x - 1][y - 1] +  matrix[x - 1][y]
                else:
                    matrix[x][y] = grid[x - 1][y - 1] 
        
        return matrix[-1][-1]

sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))