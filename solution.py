class Solution:
    def rev(self, nums, start, end):
        cnt = 0
        for i in range(end):
            if cnt == (end - start) // 2:
                return
            nums[start + i], nums[end - i - 1] = nums[end - i - 1], nums[start + i]
            cnt += 1
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dest = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dest = i
                break
        
        if dest == -1:
            self.rev(nums, 0, len(nums))
            return
        
        bigger = float('inf')
        destTwo = 0

        for i in range(dest + 1, len(nums)):
            if nums[i] <= bigger and nums[i] > nums[dest]:
                destTwo = i
                bigger = nums[i]
        
        nums[destTwo], nums[dest] = nums[dest], nums[destTwo]
        
        self.rev(nums, dest + 1, len(nums))
        
        