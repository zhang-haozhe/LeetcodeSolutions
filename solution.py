class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        
        length = 1
        left = 0
        right = 1
        
        while right < len(arr):
            if right % 2 == 0:
                if arr[right] < arr[right - 1]:
                    length = max(length, right - left + 1)
                    right += 1
                else:
                    left = right
                    right += 1
            else:
                if arr[right] > arr[right - 1]:
                    length = max(length, right - left + 1)
                    right += 1
                else:
                    left = right
                    right += 1
        
        left = 0
        right = 1
        while right < len(arr):
            if right % 2 == 0:
                if arr[right] > arr[right - 1]:
                    length = max(length, right - left + 1)
                    right += 1
                else:
                    left = right
                    right += 1
            else:
                if arr[right] < arr[right - 1]:
                    length = max(length, right - left + 1)
                    right += 1
                else:
                    left = right
                    right += 1
                    
        return length