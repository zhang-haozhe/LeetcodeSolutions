class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if not arr:
            return -1
        
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] > arr[mid - 1]:
                start = mid
            else:
                end = mid
        if arr[start] > arr[end]:
            return start
        return end