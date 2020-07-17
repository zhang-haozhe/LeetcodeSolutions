class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return len(nums) 
        count = 0
        temp = nums[0]
        prev = None
        while True:
            prev = temp
            count += 1
            if count == len(nums):
                return count
            temp = nums[count]
            # print(prev, temp)
            if prev == temp:
                del nums[count - 1]
                count -= 1