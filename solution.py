class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mapping = dict()
        mapping['b'] = 0
        mapping['a'] = 0
        mapping['l'] = 0
        mapping['o'] = 0
        mapping['n'] = 0
        for letter in text:
            if letter == 'b' or 'a' or 'l' or 'o' or 'n':
                if letter in mapping:
                    mapping[letter] += 1
        
        mapping['l'] //= 2
        mapping['o'] //= 2
        
        return min(mapping['b'], mapping['a'], mapping['l'], mapping['o'], mapping['n'])