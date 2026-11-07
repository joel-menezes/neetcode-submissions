class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i,x in enumerate(strs):
            y = list(x)
            y.sort()
            sorts = "".join(y)
            if sorts not in dic:
                dic[sorts] = [strs[i]]
            else:
                dic[sorts].append(strs[i])
        r = []
        for i in dic.values():
            r.append(i)

        return r