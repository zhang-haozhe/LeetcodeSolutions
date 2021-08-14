class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for m in range(len(matrix)):
            shouldSetRowToZero = False
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    shouldSetRowToZero = True
                    break
            if shouldSetRowToZero:
                for n in range(len(matrix[0])):
                    if matrix[m][n] != 0:
                        matrix[m][n] = '%'
        
        for n in range(len(matrix[0])):
            shouldSetColToZero = False
            for m in range(len(matrix)):
                if matrix[m][n] == 0:
                    shouldSetColToZero = True
                    break
            if shouldSetColToZero:
                for m in range(len(matrix)):
                    if matrix[m][n] != 0:
                        matrix[m][n] = '%'
        
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == '%':
                    matrix[m][n] = 0