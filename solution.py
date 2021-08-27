class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#':
            return True
        try:
            arr = preorder.split(',')
            stack = []
            for index, node in enumerate(arr):
                if node == '#':
                    if not stack[-1][1]:
                        stack[-1][1] = True
                    elif not stack[-1][2]:
                        stack[-1][2] = True
                    else:
                        return False
                while stack and stack[-1][1] and stack[-1][2]:
                    stack.pop()
                    if stack and not stack[-1][1]:
                        stack[-1][1] = True
                    elif stack and not stack[-1][2]:
                        stack[-1][2] = True
                    else:
                        return False if index != len(arr) - 1 else True
                if node != '#':
                    stack.append([node, False, False])
            return True if not stack else False
        except:
            return False
