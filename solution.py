class Solution:
    """
    @param n: the number of disks
    @return: the order of moves
    """
    def towerOfHanoi(self, n):
        # write your code here
        moves = list()
        self.helper(n, 'A', 'C', 'B', moves)
        return moves
    
    def move(self, start, end):
        return "from " + start + " to " + end

    def helper(self, n, start, end, temp, moves):
        if n == 1:
            moves.append(self.move(start, end))
            return  
        
        self.helper(n - 1, start, temp, end, moves)
        moves.append(self.move(start, end))
        self.helper(n - 1, temp, end, start, moves)