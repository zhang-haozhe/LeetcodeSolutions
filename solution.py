class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 2:
            return nums

        i, j , k = l - 2, l - 1, l - 1
        # find the first increasing position
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        if i >= 0:
            # find the first element in [j, end) that is bigger than i and swap nums[i] and nums[k]
            while nums[i] >= nums[k]:
                k -= 1
            nums[k], nums[i] = nums[i], nums[k]
        # reverse [j, end)
        nums[j:] = nums[j:][::-1]