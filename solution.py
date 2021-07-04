from copy import deepcopy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.recursion(nums)
    
    def recursion(self, nums):
        if len(nums) == 2:
            return [nums, nums[::-1]]
        elif len(nums) < 2:
            return [nums]
        else:
            subArrays = self.recursion(nums[1:])
            head = nums[0]
            
            perm = list()
            for i in range(len(subArrays)):
                for j in range(len(subArrays[0]) + 1):
                    temp = deepcopy(subArrays[i]) 
                    temp.insert(j, head)
                    perm.append(temp)
            
            return perm