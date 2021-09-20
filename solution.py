class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        peakIdx = self.findPivot(nums)
        left = self.bs(nums[:peakIdx], target)
        right = self.bs(nums[peakIdx:], target)
        
        if left != -1:
            return left
        if right != -1:
            return right + peakIdx
        return -1

    def bs(self, arr, target):
        if not arr:
            return -1
        
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] < target:
                start = mid
            else:
                end = mid
        
        if arr[start] == target:
            return start
        if arr[end] == target:
            return end
        return -1

    def findPivot(self, arr) -> int:
        if not arr:
            return -1
        
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] > arr[end]:
                start = mid
            else:
                end = mid
        return end
    