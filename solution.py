class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        idx = 0
        dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        # north, west, south, east
        pos = [0, 0]
        
        for j in range(4):
            for char in instructions:
                if char == 'G':
                    for i in range(2):
                        pos[i] += dirs[idx][i]
                else:
                    idx = (idx + 1) % 4
                    if char == 'R':
                        idx = (idx + 2) % 4
            if pos == [0, 0]:
                return True
        
        return False
            