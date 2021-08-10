class Solution:
    def quickSelect(self, k, nums, start, end):
        if start == end:
            return nums[start]
        
        i, j = start, end
        pivot = nums[(i + j) // 2]

        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        if start + k - 1 <= j:
            return self.quickSelect(k, nums, start, j)
        if start + k - 1 >= i:
            return self.quickSelect(k - (i - start), nums, i, end)
        
        return nums[j + 1]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        return self.quickSelect(k, nums, 0, len(nums) - 1)