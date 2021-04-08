class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prodLeft = [1] * length
        prodRight = [1] * length
        
        for i in range(1, length):
            prodLeft[i] = prodLeft[i - 1] * nums[i - 1]
            prodRight[-i - 1] = prodRight[-i] * nums[-i]
        
        prod = [prodLeft[x] * prodRight[x] for x in range(length)]
        return prod