class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = [nums[0]]
        for i in range(1, len(nums)):
            total.append(total[i - 1] + nums[i])
        return total
