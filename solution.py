class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letters = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], \
                   ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        
        output = []
        
        self.helper(digits, letters, output)
        
        return output
    
    def helper(self, digits, letters, output, combination='', index=0):
        if index == len(digits):
            output.append(combination)
            return
        
        letterIndex = int(digits[index])
        for letter in letters[letterIndex]:
            combination += letter
            self.helper(digits, letters, output, combination, index + 1)
            combination = combination[:-1]