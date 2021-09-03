class Solution:
    def countArrangement(self, n: int) -> int:
        cnt = 0
        nums = list(range(1, 1 + n))
        
        return self.helper(nums, cnt)
    
    def helper(self, nums, cnt, index=0, perm=[]):
        if not nums:
            cnt += 1
            return cnt
        
        total = 0
        for i in range(len(nums)):
            if nums[i] % (index + 1) == 0 or (index + 1) % nums[i] == 0:
                total += self.helper(nums[:i] + nums[i + 1:], cnt, index + 1)

        return total