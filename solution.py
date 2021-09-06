class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        maximum = 0
        longest = "."
        
        for i, v in enumerate(releaseTimes):
            if i == 0:
                maximum = v
                longest = keysPressed[i]
                continue
            
            if v - releaseTimes[i - 1] > maximum:
                maximum = v - releaseTimes[i - 1]
                longest = keysPressed[i]
                continue
                
            if v - releaseTimes[i - 1] == maximum:
                if keysPressed[i] > keysPressed[i - 1]:
                    longest = keysPressed[i]
                else:
                    longest = keysPressed[i - 1]
                    
        
        return longest