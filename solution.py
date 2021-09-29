class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        target = len(nums)
        while cnt < target:
            if nums[cnt] == 0:
                nums.append(nums.pop(cnt))
                cnt -= 1
                target -= 1
            cnt += 1