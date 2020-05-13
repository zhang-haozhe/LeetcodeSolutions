class Solution:

    def addBinary(self, a: str, b: str) -> str:
        # make the given strings of the same length
        lenA = len(a)
        lenB = len(b)
        if lenA > lenB:
            temp = ""
            for x in range(lenA - lenB):
                temp += "0"
            b = temp + b
        elif lenA < lenB:
            temp = ""
            for x in range(lenB - lenA):
                temp += "0"
            a = temp + a

        # basic binary addition

        cout = 0
        result = ""

        lenA = len(a)
        for x in range(lenA - 1, -1, -1):
            if(int(a[x]) + int(b[x]) + cout == 3):
                result = "1" + result
                cout = 1
            elif(int(a[x]) + int(b[x]) + cout == 2):
                result = "0" + result
                cout = 1
            elif(int(a[x]) + int(b[x]) + cout == 1):
                result = "1" + result
                cout = 0
            else:
                result = "0" + result
                cout = 0
        if(cout == 1):
            result = "1" + result

        return result
