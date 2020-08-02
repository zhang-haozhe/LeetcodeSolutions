class Solution:
    def frequencySort(self, s: str) -> str:
        dictionary = {}
        temp = ""
        for char in s:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        sorted_list = sorted(dictionary.items(),
                             key=lambda x: x[1], reverse=True)
        print(sorted_list)
        for n in range(len(sorted_list)):
            temp += sorted_list[n][0] * sorted_list[n][1]
        return temp
