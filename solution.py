
class Solution:

    def climbStairs(self, n: int) -> int:
        # if n == 1 or n == 0:
        #     return 1
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        #         Brute force
        first = 1
        second = 2
        if(n == 1):
            return 1
        if(n == 2):
            return 2
        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return(third)
