class Solution:
    def findLengthOfLCIS(self, A: List[int]) -> int:
        if not A:
            return 0
        longest, incr = 1, 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                incr += 1
            else:
                incr = 1
            longest = max(longest, incr)
        return longest