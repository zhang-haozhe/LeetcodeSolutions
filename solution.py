class Solution:
    def countDigitOne(self, n: int) -> int:
        base = 1
        res = 0
        
        while base <= n:
            a = n // base
            b = n % base
            curr = a % 10
            a //= 10
            
            if curr == 1:
                res += a * base + b + 1
            elif curr < 1:
                res += a * base
            else:
                res += (a + 1) * base
            
            base *= 10
        
        return res