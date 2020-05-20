class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = len(nums)- 1
        for each in range(x, 0 - 1, -1):
            if nums[each] == val:
                nums.pop(each)
        
        return len(nums)
