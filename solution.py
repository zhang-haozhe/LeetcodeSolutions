from itertools import combinations
class Solution:
    def recur(self, nums, level, output):
        if level > len(nums):
            return output
        
        for i in combinations(nums, level):
            output.append(list(i))
        
        return self.recur(nums, level + 1, output)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        output = self.recur(nums, 1, output)
        output.append([])
        return output