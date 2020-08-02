class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for n in nums:
            if n in dictionary:
                return True
            else:
                dictionary[n] = 1
        return False
