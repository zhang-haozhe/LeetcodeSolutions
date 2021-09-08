class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        arr = list(s)
        totalShifts = sum(shifts) 
        for i in range(len(arr)):
            temp = ord(arr[i])
            temp += totalShifts % 26
            if temp > ord('z'):
                temp = (temp - ord('a')) % 26 + ord('a')
            arr[i] = chr(temp)
            totalShifts -= shifts[i]
        
        output = "".join(arr)
        return output