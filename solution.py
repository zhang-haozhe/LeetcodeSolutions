from typing import List


class Solution:
    """
    brute force solution. does not pass the run time test.
    """
    # def recur(self, obstacleGrid: List[List[int]], lenx, leny, x = 0, y = 0):
    #     if x == lenx or y == leny or obstacleGrid[x][y] == 1:
    #         return 0
    #     elif x == lenx - 1 and y == leny - 1:
    #         return 1
    #     return self.recurr(obstacleGrid, lenx, leny, x + 1, y) + self.recurr(obstacleGrid, lenx, leny, x, y + 1)
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     return self.recurr(obstacleGrid, len(obstacleGrid), len(obstacleGrid[0]))
    
    """
    memoization. does not pass the run time test.
    """
    # def recurr(self, map, obstacleGrid: List[List[int]], lenx, leny, x = 0, y = 0):
    #     key = str(x) + " " + str(y)
    #     if key in map:
    #         return map[key]
        
    #     if x == lenx or y == leny or obstacleGrid[x][y] == 1:
    #         map[key] = 0
    #         return 0
    #     elif x == lenx - 1 and y == leny - 1:
    #         map[key] = 1
    #         return 1
    #     return self.recurr(map, obstacleGrid, lenx, leny, x + 1, y) + self.recurr(map, obstacleGrid, lenx, leny, x, y + 1)
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     return self.recurr(dict(), obstacleGrid, len(obstacleGrid), len(obstacleGrid[0]))

    """dynamic programming"""
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[-1][-1] == 1:
            return 0

        model = []
        for _ in range(len(obstacleGrid) + 1):
            model.append([0] * (len(obstacleGrid[0]) + 1))
        
        model[0][1] = 1
        # to help processing the data, i am adding an additional row and an additional column. to the original matrix' top and left, respectively.
        # to initialize the matrix, i set the cell above the first processed cell to 1, such that the initial cell is initialized to 1.

        for x in range(1, len(model)):
            for y in range(1, len(model[0])):
                # up = model[x - 1][y]
                # left = model[x][y - 1]

                model[x][y] += 0 if x - 2 >= 0 and y - 1 >= 0 and obstacleGrid[x - 2][y - 1] == 1 else model[x - 1][y]
                model[x][y] += 0 if x - 1 >= 0 and y - 2 >= 0 and obstacleGrid[x - 1][y - 2] == 1 else model[x][y - 1]
                # if x - 2 >= 0 and y - 1 >= 0 and obstacleGrid[x - 2][y - 1] == 1:
                #     up = 0

                # if x - 1 >= 0 and y - 2 >= 0 and obstacleGrid[x - 1][y - 2] == 1:
                #     left = 0
                
                # model[x][y] = up + left
        
        return model[-1][-1]


sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))