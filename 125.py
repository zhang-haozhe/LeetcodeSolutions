class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        s = s.lower()
        b = ""
        # convert the string to lower case for further comparison
        for each in s:
            if each.islower() or each.isnumeric():
                b += each
        # grab only letters and numbers from the string
        for x in range(len(b)//2):
            
            if(b[x] != b[len(b) - 1 - x]):
                return False
        # compare the head and the tail of the string
        return True