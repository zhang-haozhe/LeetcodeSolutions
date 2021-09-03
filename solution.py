class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        self.helper(sorted(nums), perms)
        return perms
    
    def helper(self, nums, perms, perm=[]):
        if not nums:
            perms.append(list(perm))
            return
        
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            perm.append(nums[i])
            self.helper(nums[:i] + nums[i + 1:], perms, perm)
            perm.pop()