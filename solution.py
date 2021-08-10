class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return
        
        arr = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1, arr)
    def mergeSort(self, nums, start, end, arr):
        if start == end:
            return
        
        self.mergeSort(nums, start, (start + end) // 2, arr)
        self.mergeSort(nums, (start + end) // 2 + 1, end, arr)
        self.merge(nums, start, end, arr)
    
    def merge(self, nums, start, end, arr):
        mid = (start + end) // 2
        leftIndex = start
        rightIndex = mid + 1
        index = leftIndex

        while leftIndex <= mid and rightIndex <= end:
            if nums[leftIndex] < nums[rightIndex]:
                arr[index] = nums[leftIndex]
                leftIndex += 1
            else:
                arr[index] = nums[rightIndex]
                rightIndex += 1
            index += 1
        
        while leftIndex <= mid:
            arr[index] = nums[leftIndex]
            leftIndex += 1
            index += 1
        
        while rightIndex <= end:
            arr[index] = nums[rightIndex]
            rightIndex += 1
            index += 1
        
        for i in range(start, end + 1):
            nums[i] = arr[i]