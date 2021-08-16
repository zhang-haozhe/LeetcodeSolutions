class NumArray:

    def __init__(self, nums: List[int]):
        self.sumArr = nums
        for i, k in enumerate(self.sumArr):
            if i != 0:
                self.sumArr[i] += self.sumArr[i - 1]
        print(self.sumArr)

    def sumRange(self, left: int, right: int) -> int:
        if left - 1 < 0:
            start = 0
        else:
            start = self.sumArr[left - 1]
        end = self.sumArr[right]
        
        return end - start
