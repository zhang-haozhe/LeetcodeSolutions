class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for n in nums:
            if n >= target:
                return nums.index(n)

        else:
            return len(nums)
