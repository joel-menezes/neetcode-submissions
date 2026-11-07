class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i,x in enumerate(strs):
            anagram = "".join(sorted(x))
            if anagram not in dic:
                dic[anagram] = [x]
            else:
                dic[anagram].append(x)
        returnable = []

        for i in dic.values():
            returnable.append(i)
        return returnable