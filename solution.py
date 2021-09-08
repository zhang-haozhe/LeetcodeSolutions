class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        self.helper(candidates, output, target)
        return output
    
    def helper(self, candidates, output, target, index=0, combination=[]):
        if target < 0:
            return
        if target == 0:
            output.append(list(combination))
            return
        
        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.helper(candidates, output, target - candidates[i], i, combination)
            combination.pop()
            