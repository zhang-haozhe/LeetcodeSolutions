class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in s:
            if s_dict.get(char) != None:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for char in t:
            if t_dict.get(char) != None:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        return (s_dict == t_dict)
