class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1]:
                start = mid
            else:
                end = mid
        if nums[start] > nums[end]:
            return start
        return end