def binarySearch(nums, target):
        # write your code here
        if len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1