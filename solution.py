from copy import deepcopy

# Solution 1
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

# Solution 2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        perms = []
        self.helper(nums, perms)
        return perms
    
    def helper(self, nums, perms, perm=[]):
        if not nums:
            perms.append(list(perm))
            return
        
        for i in range(len(nums)):
            perm.append(nums[i])
            self.helper(nums[:i] + nums[i + 1:], perms, perm)
            perm.pop()