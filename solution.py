class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        new_arr = ["".join(sorted(x)) for x in strs]
        
        the_map = {}
        
        for i, x in enumerate(new_arr):
            if x in the_map:
                the_map[x].append(i)
            else:
                the_map[x] = [i]
        
        res = []
        for arr in the_map.values():
            temp = []
            for elem in arr:
                temp.append(strs[elem])
            res.append(temp)
        
        return res