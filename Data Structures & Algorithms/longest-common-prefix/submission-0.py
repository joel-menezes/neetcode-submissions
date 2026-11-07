class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dic = {}
        for st in strs:
            a = ""
            for s in st:
                a += s
                if a not in dic:
                    dic[a] = 1
                else:
                    dic[a] += 1
        
        sorts = sorted(dic, key= lambda x: (dic[x], len(x)), reverse = True)
        if dic and dic[sorts[0]] != len(strs):
            return ""
        elif not dic:
            return ""
        return sorts[0]