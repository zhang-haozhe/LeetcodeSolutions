class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        self.helper(sorted(candidates), output, target)
        return output
    
    def helper(self, candidates, output, target, index=0, combination=[]):
        if target < 0 or index > len(candidates):
            return
        if target == 0:
            output.append(list(combination))
            return
        
        for i in range(index, len(candidates)):
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            combination.append(candidates[i])
            self.helper(candidates, output, target - candidates[i], i + 1, combination)
            combination.pop()
            