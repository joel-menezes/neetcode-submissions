class Solution:
    def isValid(self, s: str) -> bool:
        OPPERATORS = {"(": ")", "{": "}", "[": "]"}
        stack = []
        Popable = ""
        for i in s:
            if i in OPPERATORS:
                stack.append(i)
                Popable = stack[-1]
            else:
                if Popable and i == OPPERATORS[Popable]:
                    stack.pop()
                    if stack == []:
                        Popable = ""
                    else:
                        Popable = stack[-1]
                else:
                    return False
        return True and len(stack) == 0