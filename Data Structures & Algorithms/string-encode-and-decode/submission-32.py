class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s 

    def decode(self, s: str) -> List[str]:
        a = []
        while s:
            print(s)
            j = 0
            for i in s:
                if i == "#":
                    break
                j += 1
            a.append(s[j + 1:int(s[:j]) + 1 + j])
            s = s[int(s[:j]) + 1 + j:]
            print(s)
            print(a)
        return a

